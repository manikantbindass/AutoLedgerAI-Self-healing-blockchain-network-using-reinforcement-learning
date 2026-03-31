import numpy as np
from sklearn.ensemble import IsolationForest

class AnomalyDetector:
    def __init__(self, contamination_rate: float = 0.05):
        self.model = IsolationForest(contamination=contamination_rate, random_state=42)
        self.is_trained = False
        self.training_data = []

    def log_behavior(self, tx_rate: float, latency: float, error_rate: float):
        self.training_data.append([tx_rate, latency, error_rate])

    def train(self):
        if len(self.training_data) > 10:
            X = np.array(self.training_data)
            self.model.fit(X)
            self.is_trained = True
            
    def predict(self, feature_vector: list) -> int:
        if not self.is_trained:
            return 1
        return self.model.predict(np.array(feature_vector).reshape(1, -1))[0]
