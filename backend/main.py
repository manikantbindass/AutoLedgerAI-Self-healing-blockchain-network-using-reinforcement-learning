from fastapi import FastAPI, WebSocket, HTTPException
import asyncio
from pydantic import BaseModel
from typing import List, Dict
import random

app = FastAPI(title="AutoLedgerAI Backend")

class TransactionPayload(BaseModel):
    sender: str
    receiver: str
    amount: float

mock_network_state = {
    "nodes": [
        {"id": "node_1", "trust_score": 95.0, "status": "active", "is_malicious": False},
        {"id": "node_2", "trust_score": 80.0, "status": "active", "is_malicious": False},
        {"id": "node_3", "trust_score": 45.0, "status": "active", "is_malicious": True},
        {"id": "node_4", "trust_score": 10.0, "status": "isolated", "is_malicious": True}
    ],
    "transactions": [],
    "consensus_health": 88.5
}

@app.get("/")
def read_root():
    return {"message": "Welcome to AutoLedgerAI"}

@app.get("/nodes")
def get_nodes():
    return {"nodes": mock_network_state["nodes"]}

@app.post("/transactions")
def add_transaction(tx: TransactionPayload):
    tx_data = tx.model_dump()
    mock_network_state["transactions"].append(tx_data)
    return {"status": "success", "tx": tx_data}

@app.get("/consensus")
def get_consensus_state():
    return {"health": mock_network_state["consensus_health"]}

@app.websocket("/ws/dashboard")
async def dashboard_websocket(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            for node in mock_network_state["nodes"]:
                if node["status"] == "active":
                    delta = random.uniform(-2, 2)
                    if node["is_malicious"]:
                        delta -= 5
                    node["trust_score"] = max(0, min(100, node["trust_score"] + delta))
                    if node["trust_score"] < 30:
                        node["status"] = "isolated"
            
            await websocket.send_json(mock_network_state)
            await asyncio.sleep(2)
    except Exception as e:
        print(f"WebSocket Error: {e}")
