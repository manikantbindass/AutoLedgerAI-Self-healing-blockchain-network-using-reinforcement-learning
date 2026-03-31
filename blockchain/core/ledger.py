from typing import List
from .block import Block
from .transaction import Transaction

class LedgerState:
    def __init__(self):
        self.chain: List[Block] = []
        self.pending_transactions: List[Transaction] = []
        self.accounts = {}
        
    def add_block(self, block: Block) -> bool:
        if len(self.chain) > 0:
            last_block = self.chain[-1]
            if block.previous_hash != last_block.hash:
                return False
            if block.index != last_block.index + 1:
                return False
        
        self.chain.append(block)
        for tx in block.transactions:
            self.accounts[tx.sender] = self.accounts.get(tx.sender, 0) - tx.amount
            self.accounts[tx.receiver] = self.accounts.get(tx.receiver, 0) + tx.amount
            self.pending_transactions = [p for p in self.pending_transactions if p.tx_hash != tx.tx_hash]
            
        return True

    def get_balance(self, address: str) -> float:
        return self.accounts.get(address, 0.0)
