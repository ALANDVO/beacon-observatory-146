import pytest
from fastapi.testclient import TestClient
import sys
import os

# Add backend directory to path so tests can import from there
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend')))

from main import app

client = TestClient(app)

def test_root_endpoint():
    """Test the root endpoint returns welcome message"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "DeepTutor API" in data["message"]

def test_health_check():
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "timestamp" in data

def test_hello_get():
    """Test GET /api/hello endpoint"""
    response = client.get("/api/hello")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "success" in data["message"]

def test_hello_post():
    """Test POST /api/hello endpoint"""
    test_data = {"name": "TestUser"}
    response = client.post("/api/hello", json=test_data)
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "TestUser" in data["message"]

def test_greet_name():
    """Test GET /api/greet/{name} endpoint"""
    response = client.get("/api/greet/John")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "John" in data["message"]

def test_greet_empty_name():
    """Test GET /api/greet/{name} with empty name"""
    response = client.get("/api/greet/")
    assert response.status_code == 404
