class TrustManager:
    def __init__(self, initial_trust: float = 100.0, min_trust: float = 0.0, max_trust: float = 100.0):
        self.initial_trust = initial_trust
        self.min_trust = min_trust
        self.max_trust = max_trust
        self.trust_scores = {}

    def get_trust(self, node_id: str) -> float:
        return self.trust_scores.get(node_id, self.initial_trust)

    def update_trust(self, node_id: str, delta: float):
        current = self.get_trust(node_id)
        new_score = max(self.min_trust, min(self.max_trust, current + delta))
        self.trust_scores[node_id] = new_score

    def penalize_node(self, node_id: str, penalty: float):
        self.update_trust(node_id, -abs(penalty))

    def reward_node(self, node_id: str, reward: float):
        self.update_trust(node_id, abs(reward))

    def is_trusted(self, node_id: str, threshold: float = 30.0) -> bool:
        return self.get_trust(node_id) >= threshold
