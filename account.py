from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# User data
users = {
    "Syeda": {"pin": 1111, "balance": 50000},
    "Shah": {"pin": 2222, "balance": 0}
}

# Store authenticated users
authenticated_users = set()

# Single user authentication request model
class AuthRequest(BaseModel):
    name: str
    pin_number: int

# Multiple authentication request model
class MultiAuthRequest(BaseModel):
    users: List[AuthRequest]

# Bank transfer request model
class TransferRequest(BaseModel):
    sender_name: str
    recipient_name: str
    amount: int

# Authenticate a single user
@app.post("/authenticate")
def authenticate_user(data: AuthRequest):
    name = data.name
    pin = data.pin_number
    if name in users and users[name]["pin"] == pin:
        authenticated_users.add(name)
        return {"message": f"{name} authenticated", "balance": users[name]["balance"]}
    return {"error": "Invalid name or pin"}

# Authenticate multiple users at once
@app.post("/authenticate-both")
def authenticate_both(data: MultiAuthRequest):
    authenticated = []
    for user in data.users:
        name = user.name
        pin = user.pin_number
        if name in users and users[name]["pin"] == pin:
            authenticated_users.add(name)
            authenticated.append({"name": name, "balance": users[name]["balance"]})
        else:
            return {"error": f"Invalid credentials for {name}"}
    return {"message": "All users authenticated", "authenticated": authenticated}

# Bank transfer endpoint
@app.post("/bank-transfer")
def bank_transfer(data: TransferRequest):
    sender = data.sender_name
    receiver = data.recipient_name
    amount = data.amount

    # Check authentication
    if sender not in authenticated_users:
        return {"error": "Sender not authenticated"}

    # Validate users
    if sender not in users or receiver not in users:
        return {"error": "User not found"}

    # Check balance
    if users[sender]["balance"] < amount:
        return {"error": "Insufficient funds"}

    # Process transfer
    users[sender]["balance"] -= amount
    users[receiver]["balance"] += amount

    return {
        "message": f"Transferred {amount} from {sender} to {receiver}",
        "sender_balance": users[sender]["balance"],
        "receiver_balance": users[receiver]["balance"]
    }

# Get balance of a single user
@app.get("/balance/{name}")
def get_user_balance(name: str):
    if name in users:
        return {"name": name, "balance": users[name]["balance"]}
    return {"error": "User not found"}

# Get updated balances for both users
@app.get("/update-accounts")
def get_updated_accounts():
    return {
        "Syeda": users["Syeda"],
        "Shah": users["Shah"]
    }
