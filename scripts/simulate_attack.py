import time
import requests
import random

API_URL = "http://localhost:8000"

def simulate():
    print("Starting Sybil Attack Simulation...")
    
    for _ in range(20):
        sender = "hacker_node"
        receiver = f"target_{random.randint(1,10)}"
        amount = random.uniform(10, 1000)
        
        try:
            res = requests.post(f"{API_URL}/transactions", json={
                "sender": sender,
                "receiver": receiver,
                "amount": amount
            })
            print(f"Spam tx sent: {res.status_code}")
        except Exception as e:
            print("API not reachable yet...")
        
        time.sleep(0.5)
        
    print("Attack complete.")

if __name__ == "__main__":
    simulate()
