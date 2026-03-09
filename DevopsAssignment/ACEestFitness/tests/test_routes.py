import json
from app.routes import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to ACEest Fitness" in response.data

def test_get_members():
    client = app.test_client()
    response = client.get("/members")
    data = json.loads(response.data)
    assert isinstance(data, list)
    assert "name" in data[0]

def test_add_member():
    client = app.test_client()
    response = client.post("/members", json={"name": "John", "membership": "Platinum"})
    data = json.loads(response.data)
    assert response.status_code == 201
    assert data["name"] == "John"
