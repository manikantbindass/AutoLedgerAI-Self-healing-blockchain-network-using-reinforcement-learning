# AutoLedgerAI - Self-Healing Blockchain Network using Reinforcement Learning

AutoLedgerAI is a decentralized blockchain network that utilizes Machine Learning and Reinforcement Learning (RL) to dynamically adjust consensus parameters, detect malicious nodes, and self-heal against Sybil and spam attacks in real-time.

## Architecture Diagram
```text
Client -> (React/Tailwind Dashboard) -> [FastAPI Backend] <-> (Blockchain / RL Environment)
                                             |
                                     (PostgreSQL + Kafka)
```

## Features
- **RL-controlled Consensus**: Dynamically adjusts required voting power and penalizes malicious node behavior using PyTorch-based PPO logic.
- **Anomaly Detection**: Uses Scikit-learn (Isolation Forest) and NetworkX for graph anomaly detection to identify Sybil node rings.
- **Microservices Setup**: Fully containerized with Docker, Kafka stream handling, and robust DB architecture.
- **Premium Real-Time Dashboard**: Aesthetic monitoring of node behavior, health metrics, and ledger visualization over WebSockets.

## Setup Steps
1. Make sure you have Docker Desktop and Python 3.10+ installed.
2. Clone this repository.
3. Apply configurations from `.env.example` if needed.
4. Run:
   ```bash
   docker-compose up --build
   ```
5. View the dashboard at `http://localhost:3000`.

## Demo Instructions
Once the system is up and running via Docker, you can simulate an attack. Open a new terminal and run:
   ```bash
   pip install requests
   python scripts/simulate_attack.py
   ```
Observe the real-time adjustments on the dashboard where "malicious_activity" is flagged and the attacker's node trust score drops, eventually isolating them from consensus validations.
