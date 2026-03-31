import time
import requests
import random

API_URL = "http://localhost:8000"

def run_normal():
    print("Simulating Normal Network Behavior...")
    for _ in range(50):
        sender = f"user_{random.randint(1,5)}"
        receiver = f"target_{random.randint(1,10)}"
        amount = random.uniform(0.1, 5)
        
        try:
            res = requests.post(f"{API_URL}/transactions", json={
                "sender": sender,
                "receiver": receiver,
                "amount": amount
            })
            print(f"Normal tx sent")
        except:
            pass
        
        time.sleep(1)

if __name__ == "__main__":
    run_normal()
