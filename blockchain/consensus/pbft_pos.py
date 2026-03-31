import random
from typing import Dict

class PBFT_PoS_Engine:
    def __init__(self, min_validators: int = 4):
        self.min_validators = min_validators
        self.active_nodes: Dict[str, dict] = {}

    def register_node(self, node_id: str, stake: float, trust_score: float = 100.0):
        self.active_nodes[node_id] = {
            "stake": stake,
            "trust_score": trust_score
        }

    def select_validator(self) -> str:
        if not self.active_nodes:
            return None
            
        total_weight = sum(info["stake"] * (info["trust_score"] / 100.0) 
                           for info in self.active_nodes.values())
                           
        if total_weight <= 0:
            return list(self.active_nodes.keys())[0]
            
        pick = random.uniform(0, total_weight)
        current = 0.0
        for node_id, info in self.active_nodes.items():
            weight = info["stake"] * (info["trust_score"] / 100.0)
            current += weight
            if current >= pick:
                return node_id
                
        return list(self.active_nodes.keys())[-1]

    def validate_block_pbft(self, block, signatures: dict) -> bool:
        total_nodes = len(self.active_nodes)
        if total_nodes < self.min_validators:
            return True 
            
        required_votes = (2 * total_nodes) // 3
        valid_votes = sum(1 for node_id in signatures if self.active_nodes.get(node_id, {}).get("trust_score", 0) > 30)
        
        return valid_votes >= required_votes
