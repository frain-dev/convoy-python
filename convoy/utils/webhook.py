import base64
from datetime import datetime
import hashlib
import hmac

class InvalidTimestampError(Exception):
    def __init__(self, *args: list) -> None:
        self.message = args[0]
        
    @property
    def response(self):
        return self.message


class InvalidSignature(Exception):
    def __init__(self, *args: list) -> None:
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
        
    def get_hash_function(self, hash: str) -> str:
        if str.lower(hash) == "sha256":
            return hashlib.sha256
        if str.lower(hash) == "md5":
            return hashlib.md5
        if str.lower(hash) == "sha384":
            return hashlib.sha384
        if str.lower(hash) == "sha224":
            return hashlib.sha224
        if str.lower(hash) == "sha512":
            return hashlib.sha512
        if str.lower(hash) == "sha1":
            return hashlib.sha1
        if str.lower(hash) == "sha3_256":
            return hashlib.sha3_256
        if str.lower(hash) == "sha3_224":
            return hashlib.sha3_224 
        if str.lower(hash) == "sha3_512":
            return hashlib.sha3_512 
        else:
            raise Exception("algorithm not available.")
        
    def verify_timestamp(self, timestamp):
        try:
            now = round(datetime.now().timestamp())
            timestamp_int = int(timestamp.timestamp())
            
            diff = now - self.tolerance
            
            if timestamp_int < diff:
                raise InvalidTimestampError("Timestamp is too old.")
            else:
                return True
            
        except InvalidTimestampError as e:
            return e.response

        
    def compare_hashes(self, hash1: str, hash2: str) -> bool:
        if self.encoding == "hex":
            valid = hmac.compare_digest(hash1, hash2)
            if valid is False:
                raise InvalidSignature("Invalid signature.")
            return valid                
        if self.encoding == "base64":
            valid = hmac.compare_digest(base64.b64decode(hash1), base64.b64decode(hash2))
            if valid is False:
                raise InvalidSignature("Invalid signature.")
        
        
    def create_signature(self, payload: str) -> str:
        # If the encoding is hex, create a new hex hmac digest
        if self.encoding == "hex":
            return hmac.new(bytes(self.secret, "utf-8"), msg=bytes(payload, "utf-8"), digestmod=self.hash).hexdigest()
        
        # If the encoding is base64, create a new base64 hmac digest
        if self.encoding == "base64":
            sig = hmac.new(bytes(self.secret, "utf-8"), msg=bytes(payload, "utf-8"), digestmod=self.hash).digest()
            return base64.b64encode(sig).decode()
        
    def get_timestamp_and_signatures(self, signature):
        signature = signature.split(",")
        signature = [sig.split("=", 1) for sig in signature]
                    
        timestamp_int = int(signature[0][1]) if signature[0][0] == "t" else None
        
        if timestamp_int is not None:
            timestamp = datetime.fromtimestamp(timestamp_int)
            
        return (timestamp, signature[1])
    
                
    def verify_signature(self, payload: str, signature: str) -> bool:
        is_advanced = len(signature.split(",")) > 1
        
        if is_advanced:
            return self.verify_advanced_signature(payload, signature)
        
        return self.verify_simple_signature(payload, signature)
    
    def verify_simple_signature(self, payload: str, signature: str) -> bool:
        try:
            return self.compare_hashes(self.create_signature(payload), signature)
        except InvalidSignature as e:
            return e.response

    def verify_advanced_signature(self, payload: str, signature: str) -> bool:
        timestamp, signature = self.get_timestamp_and_signatures(signature)

        try:            
            if self.verify_timestamp(timestamp) is False:
                raise InvalidTimestampError("Invalid timestamp.")
            else: 
                return self.compare_hashes(self.create_signature(payload), signature[1])

        except (InvalidTimestampError, InvalidSignature) as e:
            return e.response
