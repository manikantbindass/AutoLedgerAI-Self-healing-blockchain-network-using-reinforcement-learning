import torch
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from rl_agent.environment.blockchain_env import BlockchainEnv
from rl_agent.models.ppo_agent import PPOActorCritic

def train():
    env = BlockchainEnv()
    model = PPOActorCritic(num_inputs=env.observation_space.shape[0], num_outputs=env.action_space.n)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
    
    print("Starting Training...")
    for epoch in range(100):
        state, _ = env.reset()
        for _ in range(50):
            action, log_prob, value = model.get_action(state)
            next_state, reward, terminated, truncated, _ = env.step(action)
            
            optimizer.zero_grad()
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            target = reward + 0.99 * model.critic(torch.FloatTensor(next_state).unsqueeze(0)).detach()
            value_loss = torch.nn.functional.mse_loss(model.critic(state_tensor), target)
            value_loss.backward()
            optimizer.step()
            
            state = next_state

        if epoch % 20 == 0:
            print(f"Epoch {epoch} completed.")

    torch.save(model.state_dict(), "ppo_latest.pth")
    print("Model saved")

if __name__ == "__main__":
    train()
