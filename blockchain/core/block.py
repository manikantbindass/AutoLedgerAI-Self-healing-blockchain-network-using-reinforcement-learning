import hashlib
import time
import json
from typing import List
from .transaction import Transaction

class Block:
    def __init__(self, index: int, previous_hash: str, transactions: List[Transaction], 
                 validator: str, validator_trust_score: float = 100.0):
        self.index = index
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.validator = validator
        self.validator_trust_score = validator_trust_score
        self.nonce = 0
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        tx_data = [tx.to_dict() for tx in self.transactions]
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": tx_data,
            "previous_hash": self.previous_hash,
            "validator": self.validator,
            "nonce": self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "transactions": [tx.to_dict() for tx in self.transactions],
            "previous_hash": self.previous_hash,
            "validator": self.validator,
            "hash": self.hash
        }
