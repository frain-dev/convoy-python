import base64
from datetime import datetime
import hmac

class InvalidTimestampError(Exception):
    def __init__(self, *args: list) -> None:
        self.message = args[0]
        
    @property
    def response(self):
        return self.message
    

class Webhook:
    def __init__(self, secret: str, encoding: str = "hex", tolerance: int = 300, hash: str = "sha256") -> None:
        self.secret = secret
        self.encoding = encoding
        self.tolerance = tolerance
        self.hash = hash
        
    def verify_timestamp(self, timestamp):
        try:
            now = round(datetime.now().timestamp())
            timestamp_int = int(timestamp.timestamp())
            
            print("Now: ", now)
            diff = now - self.tolerance
            
            if timestamp_int < diff:
                raise InvalidTimestampError("Timestamp is too old.")
            else:
                return True
            
        except InvalidTimestampError as e:
            return e.response

        
    def compare_hashes(self, hash1: str, hash2: str) -> bool:
        if self.encoding == "hex":
            return hash1 == hash2
        if self.encoding == "base64":
            return hmac.compare_digest(base64.b64decode(hash1), base64.b64decode(hash2))
        
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
        return self.compare_hashes(self.create_signature(payload), signature)
    
    def verify_advanced_signature(self, payload: str, signature: str) -> bool:
        timestamp, signature = self.get_timestamp_and_signatures(signature)

        try:            
            if self.verify_timestamp(timestamp) is False:
                raise InvalidTimestampError("Invalid timestamp.")
            else: 
                return self.compare_hashes(self.create_signature(payload), signature[1])

        except InvalidTimestampError as e:
            return e.response    
    