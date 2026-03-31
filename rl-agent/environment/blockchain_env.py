import gymnasium as gym
from gymnasium import spaces
import numpy as np

class BlockchainEnv(gym.Env):
    def __init__(self):
        super(BlockchainEnv, self).__init__()
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Box(low=0, high=1, shape=(4,), dtype=np.float32)
        self.state = np.array([0.8, 0.0, 0.2, 0.0], dtype=np.float32)
        
    def step(self, action):
        trust, anomaly, latency, malicious = self.state
        reward = 0.0
        if action == 0:
            malicious = min(1.0, malicious + 0.1)
            reward -= 1.0
        elif action == 2:
            malicious = max(0.0, malicious - 0.1)
            reward += 1.0
            
        self.state = np.clip(self.state + np.random.normal(0, 0.05, 4), 0, 1).astype(np.float32)
        self.state[3] = malicious
        reward += (self.state[0] - self.state[1] - self.state[3])
        
        return self.state, reward, False, False, {}

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.array([1.0, 0.0, 0.1, 0.0], dtype=np.float32)
        return self.state, {}
