# tests/test_app.py
from app import app
import json

def test_index_status_code():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200

def test_health_endpoint():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    data = json.loads(resp.data)
    assert "status" in data and data["status"] == "ok"
