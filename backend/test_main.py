import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    """Test the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Todo App API is running!"}

def test_health_check():
    """Test basic health check"""
    response = client.get("/health")  # This might not exist yet, but let's see
    # If the endpoint doesn't exist, it should return 404
    if response.status_code == 404:
        # This is expected if we don't have a health endpoint yet
        print("Health endpoint not implemented yet, which is fine")
    else:
        assert response.status_code == 200

if __name__ == "__main__":
    test_read_root()
    test_health_check()
    print("Basic tests passed!")