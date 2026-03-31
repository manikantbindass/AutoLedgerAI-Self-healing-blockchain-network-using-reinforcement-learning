<div align="center">

![Header](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20&height=300&section=header&text=AutoLedgerAI&fontSize=90&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Self-Healing%20Blockchain%20Network%20with%20Reinforcement%20Learning&descAlignY=55&descSize=25)

[![Blockchain](https://img.shields.io/badge/Blockchain-121D33?style=for-the-badge&logo=blockchain.com&logoColor=white)](https://github.com/manikantbindass/AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4EA94B?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Kafka](https://img.shields.io/badge/Apache%20Kafka-231F20?style=for-the-badge&logo=apache-kafka&logoColor=white)](https://kafka.apache.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white)](https://grafana.com/)

</div>

---

## 🎯 **Project Objective**

**AutoLedgerAI** is a production-grade, self-healing blockchain network that uses **Reinforcement Learning (RL)** agents to autonomously detect malicious nodes, adjust consensus parameters, and maintain high availability. The system assigns **adaptive trust scores** to nodes and makes intelligent decisions to ensure network security and performance.

---

## 🧠 **Core Features**

<table>
<tr>
<td width="33%" valign="top">

### 🔍 **Node Monitoring**
- Real-time transaction validation tracking
- Block propagation delay analysis  
- Voting pattern detection
- Network latency metrics
- Behavioral anomaly detection

</td>
<td width="33%" valign="top">

### ⚠️ **Malicious Detection**
- Sybil attack identification
- Double-spending prevention
- Abnormal voting detection
- Isolation Forest algorithm
- Graph-based anomaly analysis

</td>
<td width="33%" valign="top">

### 🤖 **RL Agent (DQN/PPO)**
- Dynamic consensus adjustment
- Node penalty system
- Validator reassignment
- Autonomous healing decisions
- Reward-based optimization

</td>
</tr>
</table>

---

## 🏗️ **System Architecture**

```
┌─────────────────────────────────────────────────────────────────────┐
│                         AutoLedgerAI System                          │
└─────────────────────────────────────────────────────────────────────┘

      ┌──────────────┐         ┌──────────────┐
      │  React.js    │◄────────┤  FastAPI     │
      │  Dashboard   │         │  Backend     │
      └──────────────┘         └──────┬───────┘
             ▲                        │
             │                        │
             │                ┌───────▼────────┐
             │                │  Blockchain    │
             │                │  Core (PBFT)   │
             │                └───────┬────────┘
             │                        │
      ┌──────┴──────┐         ┌───────▼────────┐
      │  Grafana    │         │  RL Agent      │
      │  Monitoring │◄────────┤  (DQN/PPO)     │
      └─────────────┘         └───────┬────────┘
                                      │
           ┌──────────────────────────┼──────────────────────────┐
           │                          │                          │
      ┌────▼────┐              ┌──────▼──────┐          ┌────────▼────┐
      │ Trust   │              │  Detection  │          │   Kafka     │
      │ System  │              │  Engine     │          │   Stream    │
      └─────────┘              └─────────────┘          └─────────────┘
                                      │
                               ┌──────▼──────┐
                               │  MongoDB    │
                               │  Database   │
                               └─────────────┘
```

---

## 🔄 **RL Decision Loop**

```
┌────────────────────────────────────────────────────────────────┐
│                   RL Agent Decision Cycle                      │
└────────────────────────────────────────────────────────────────┘

  ┌─────────────┐
  │   STATE     │  ← Node metrics, trust scores, network health
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │   AGENT     │  ← DQN/PPO Policy Network
  │  (Policy)   │
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │   ACTION    │  ← Adjust threshold, remove node, rescale validators
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │  REWARD     │  ← +1 for improved performance, -1 for attack success
  └──────┬──────┘
         │
         ▼
  ┌─────────────┐
  │ ENVIRONMENT │  ← Blockchain network state updated
  └─────────────┘
         │
         └──────► Back to STATE
```

---

## 📂 **Project Structure**

```
AutoLedgerAI/
│
├── blockchain/
│   ├── core/              # Block, Transaction, Ledger, Crypto
│   ├── consensus/         # PBFT, PoS, Consensus Manager
│   └── networking/        # P2P Node, Message Types
│
├── rl-agent/
│   ├── environment/       # Custom Gym Environment
│   ├── models/            # DQN/PPO Agent
│   └── training/          # Training Scripts
│
├── trust-system/
│   ├── scoring.py         # Dynamic Trust Score Calculation
│   └── reputation_engine.py
│
├── detection-engine/
│   └── anomaly_detection.py  # Isolation Forest, Graph Analysis
│
├── backend/
│   ├── api/               # REST & WebSocket Routes
│   └── services/          # DB, Kafka, Blockchain Client
│
├── frontend/
│   └── dashboard/         # React + TailwindCSS Dashboard
│
├── scripts/
│   ├── simulate_attack.py # Malicious Node Simulation
│   ├── node_behavior.py   # Node Behavior Generator
│   └── setup.sh           # One-Command Setup
│
├── configs/
│   ├── kafka.yml
│   ├── env.example
│   └── network_config.yml
│
└── docs/
    ├── SRS.md             # Software Requirements Spec
    ├── architecture.md    # Detailed System Design
    └── setup-guide.md     # Step-by-Step Setup
```

---

## 🚀 **Quick Start (One Command)**

```bash
# Clone the repository
git clone https://github.com/manikantbindass/AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning.git
cd AutoLedgerAI-Self-healing-blockchain-network-using-reinforcement-learning

# Run setup script (installs all dependencies and starts services)
chmod +x scripts/setup.sh
./scripts/setup.sh
```

### **Alternative: Docker Compose**

```bash
# Copy environment file
cp configs/env.example .env

# Start all services
docker-compose up --build

# Access dashboard
open http://localhost:3000
```

---

## 🧪 **Test Scenarios**

| **Attack Type**       | **Detection Method**       | **RL Action**            | **Expected Result**        |
|-----------------------|----------------------------|--------------------------|----------------------------|
| Sybil Attack          | Graph-based clustering     | Remove malicious nodes   | Network stabilizes         |
| Double Spending       | Transaction validation     | Penalize trust score     | Attack prevented           |
| Malicious Validator   | Voting pattern analysis    | Reassign validators      | Consensus maintained       |
| Node Failure          | Latency spike detection    | Trigger node recovery    | Self-healing activated     |

---

## 🔐 **Security Features**

- **SHA-256 Hashing** for block integrity
- **Digital Signatures** for transaction verification
- **RBAC** (Role-Based Access Control) for node permissions
- **End-to-End Encryption** for P2P communication
- **JWT Authentication** for API security

---

## 📊 **RL Design**

### **State Space**
- Node trust scores (n-dimensional vector)
- Transaction success rate
- Block propagation time
- Voting consistency metric

### **Action Space**
- Adjust consensus threshold (±0.1)
- Remove node from network
- Reassign validator role
- Trigger ledger re-sync

### **Reward Function**
```python
reward = (
    +1.0 * (throughput / max_throughput) +
    -0.5 * (latency / max_latency) +
    +2.0 * (successful_attack_prevention) +
    -2.0 * (false_positive_rate)
)
```

---

## 📚 **Documentation**

| File | Description |
|------|-------------|
| [SRS.md](docs/SRS.md) | Complete software requirements specification |
| [architecture.md](docs/architecture.md) | Detailed system architecture and design patterns |
| [setup-guide.md](docs/setup-guide.md) | Step-by-step installation and deployment guide |

---

## 🛠️ **Tech Stack**

| Component | Technology |
|-----------|-----------|
| **Blockchain** | Python (Custom Implementation) |
| **Consensus** | PBFT + PoS Hybrid |
| **RL Framework** | PyTorch / TensorFlow |
| **Backend** | FastAPI |
| **Frontend** | React.js + TailwindCSS |
| **Database** | MongoDB |
| **Messaging** | Apache Kafka |
| **Monitoring** | Grafana + Prometheus |
| **Containerization** | Docker + Docker Compose |

---

## 📈 **Roadmap**

- [x] Core blockchain implementation
- [x] RL agent (DQN/PPO)
- [x] Trust scoring system
- [x] Malicious node detection
- [x] Self-healing mechanism
- [ ] Multi-chain support
- [ ] Federated RL agents
- [ ] DAO governance integration
- [ ] Cross-chain healing protocols

---

## 🤝 **Contributing**

Contributions are welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 **License**

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

---

## 📧 **Contact**

**Manikant Kumar**  
📧 Email: [manikantbindass@gmail.com](mailto:manikantbindass@gmail.com)  
🔗 GitHub: [@manikantbindass](https://github.com/manikantbindass)  
💼 LinkedIn: [Manikant Kumar](https://www.linkedin.com/in/manikantbindass/)

---

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,14,16,18,20&height=150&section=footer)

**⭐ Star this repo if you find it useful!**

</div>
