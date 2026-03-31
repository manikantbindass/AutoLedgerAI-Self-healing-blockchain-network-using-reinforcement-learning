import torch
import torch.nn as nn
from torch.distributions.categorical import Categorical

class PPOActorCritic(nn.Module):
    def __init__(self, num_inputs, num_outputs, hidden_size=64):
        super(PPOActorCritic, self).__init__()
        self.critic = nn.Sequential(
            nn.Linear(num_inputs, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, 1)
        )
        self.actor = nn.Sequential(
            nn.Linear(num_inputs, hidden_size),
            nn.ReLU(),
            nn.Linear(hidden_size, num_outputs)
        )
        
    def _get_action_dist(self, state):
        logits = self.actor(state)
        return Categorical(logits=logits)
        
    def get_action(self, state):
        state = torch.FloatTensor(state).unsqueeze(0)
        dist = self._get_action_dist(state)
        action = dist.sample()
        value = self.critic(state)
        log_prob = dist.log_prob(action)
        return action.item(), log_prob.item(), value.item()
