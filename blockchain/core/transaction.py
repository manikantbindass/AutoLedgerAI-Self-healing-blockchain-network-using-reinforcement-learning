import hashlib
import time
from pydantic import BaseModel
from typing import Optional

class Transaction(BaseModel):
    sender: str
    receiver: str
    amount: float
    timestamp: float = 0.0
    tx_hash: str = ""
    signature: Optional[str] = None
    
    def __init__(self, **data):
        super().__init__(**data)
        if self.timestamp == 0.0:
            self.timestamp = time.time()
        if not self.tx_hash:
            self.tx_hash = self.compute_hash()
            
    def compute_hash(self) -> str:
        tx_data = f"{self.sender}{self.receiver}{self.amount}{self.timestamp}"
        return hashlib.sha256(tx_data.encode()).hexdigest()

    def to_dict(self):
        return self.model_dump()
