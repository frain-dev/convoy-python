import base64
from datetime import datetime
import hashlib
import hmac
import json

class InvalidTimestampError(Exception):
    def __init__(self, *args: str) -> None:
        self.message = args[0]
        
    @property
    def response(self):
        return self.message


class InvalidSignature(Exception):
    def __init__(self, *args: str) -> None:
        self.message = args[0]
        
    @property
    def response(self):
        return self.message
    

class Webhook:
    def __init__(self, secret: str = "", encoding: str = "hex", tolerance: int = 300, hash: str = "sha256") -> None:
        self.secret = secret
        self.encoding = encoding
        self.tolerance = tolerance
        self.hash = self.get_hash_function(hash)
        
    def get_hash_function(self, hash: str):
        # Convoy only ever signs with SHA256 or SHA512 (see pkg/signature).
        # Accepting weaker/other algorithms here would let a caller verify
        # against a hash the server never uses, so restrict to the contract.
        normalized = str.lower(hash)
        if normalized == "sha256":
            return hashlib.sha256
        if normalized == "sha512":
            return hashlib.sha512
        raise ValueError(f"unsupported hash algorithm: {hash!r}; expected 'sha256' or 'sha512'")
        
    def verify_timestamp(self, timestamp):
        now = round(datetime.now().timestamp())
        timestamp_int = int(timestamp.timestamp())

        if timestamp_int < now - self.tolerance:
            raise InvalidTimestampError("Timestamp is too old.")
        return True

        
    def compare_hashes(self, hash1: str, hash2: str) -> bool:
        if self.encoding == "hex":
            valid = hmac.compare_digest(hash1, hash2)
            if valid is False:
                raise InvalidSignature("Invalid signature.")
            return valid
        if self.encoding == "base64":
            try:
                decoded1 = base64.b64decode(hash1)
                decoded2 = base64.b64decode(hash2)
            except (ValueError, TypeError) as exc:
                # A malformed signature is a mismatch, not a crash.
                raise InvalidSignature("Invalid signature.") from exc
            valid = hmac.compare_digest(decoded1, decoded2)
            if valid is False:
                raise InvalidSignature("Invalid signature.")
            return valid
        raise InvalidSignature("Invalid encoding.")
        
    def _encode_payload(self, payload):
        """
        Encode payload to match Convoy's JSON format for consistent signature generation.
        
        Convoy's Go backend uses json.NewEncoder() which produces compact JSON without 
        whitespace (no spaces after colons/commas). This method ensures our JSON encoding
        matches that format using separators=(',', ':') for compatibility with both
        simple and advanced signature verification.
        """
        if isinstance(payload, dict):
            # Convert dict to JSON string and trim newline like Convoy
            json_str = json.dumps(payload, separators=(',', ':'), sort_keys=False)
            return json_str
        elif isinstance(payload, str):
            # If it's already a string, return as-is
            return payload
        else:
            # Convert to string for other types
            return str(payload)
        
    def create_signature(self, payload: str) -> str:
        """Create signature for simple webhooks (payload only)"""
        encoded_payload = self._encode_payload(payload)
        
        # If the encoding is hex, create a new hex hmac digest
        if self.encoding == "hex":
            return hmac.new(bytes(self.secret, "utf-8"), msg=bytes(encoded_payload, "utf-8"), digestmod=self.hash).hexdigest()
        
        # If the encoding is base64, create a new base64 hmac digest
        if self.encoding == "base64":
            sig = hmac.new(bytes(self.secret, "utf-8"), msg=bytes(encoded_payload, "utf-8"), digestmod=self.hash).digest()
            return base64.b64encode(sig).decode()

        # Fail closed instead of implicitly returning None.
        raise InvalidSignature("Invalid encoding.")
    
    def create_advanced_signature(self, payload, timestamp=None) -> str:
        """Create signature for advanced webhooks (timestamp + payload) like Convoy does"""
        if timestamp is None:
            timestamp = int(datetime.now().timestamp())
        
        encoded_payload = self._encode_payload(payload)
        
        # Create signed payload: timestamp + "," + payload (matching Convoy's format)
        signed_payload = f"{timestamp},{encoded_payload}"
        
        # If the encoding is hex, create a new hex hmac digest
        if self.encoding == "hex":
            return hmac.new(bytes(self.secret, "utf-8"), msg=bytes(signed_payload, "utf-8"), digestmod=self.hash).hexdigest()
        
        # If the encoding is base64, create a new base64 hmac digest
        if self.encoding == "base64":
            sig = hmac.new(bytes(self.secret, "utf-8"), msg=bytes(signed_payload, "utf-8"), digestmod=self.hash).digest()
            return base64.b64encode(sig).decode()

        # Fail closed instead of implicitly returning None.
        raise InvalidSignature("Invalid encoding.")
        
    def get_timestamp_and_signatures(self, signature):
        pairs = [sig.split("=", 1) for sig in signature.split(",")]

        timestamp_pair = next((p for p in pairs if p[0].strip() == "t"), None)
        try:
            timestamp_int = int(timestamp_pair[1])
        except (TypeError, ValueError) as exc:
            raise InvalidTimestampError("Invalid timestamp format") from exc

        timestamp = datetime.fromtimestamp(timestamp_int)
        signatures = [p[1] for p in pairs if p[0].strip() != "t" and len(p) == 2]

        return timestamp, signatures
    
                
    def verify_signature(self, payload: str, signature: str) -> bool:
        is_advanced = len(signature.split(",")) > 1
        
        if is_advanced:
            return self.verify_advanced_signature(payload, signature)
        
        return self.verify_simple_signature(payload, signature)
    
    def verify_simple_signature(self, payload: str, signature: str) -> bool:
        # Fail closed: any mismatch or malformed signature returns False, never a
        # truthy error string (which would make `if verify(...)` pass a forgery).
        try:
            return self.compare_hashes(self.create_signature(payload), signature)
        except InvalidSignature:
            return False

    def verify_advanced_signature(self, payload: str, signature: str) -> bool:
        try:
            timestamp, signatures = self.get_timestamp_and_signatures(signature)
            self.verify_timestamp(timestamp)

            expected = self.create_advanced_signature(payload, int(timestamp.timestamp()))
            for sig in signatures:
                try:
                    if self.compare_hashes(expected, sig) is True:
                        return True
                except InvalidSignature:
                    continue
            return False

        except (InvalidTimestampError, InvalidSignature):
            return False
