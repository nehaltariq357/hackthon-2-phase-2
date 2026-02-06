import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_user_success():
    """Test successful user registration"""
    # Clean up any existing test user
    import sqlite3
    conn = sqlite3.connect('todo_app.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM user WHERE email = 'test_register@example.com'")
    conn.commit()
    conn.close()

    # Now test registration
    user_data = {
        "email": "test_register@example.com",
        "password": "securepassword123"
    }
    response = client.post("/auth/register", json=user_data)

    # Should return 200 for successful registration
    print(f"Register response: {response.status_code}, {response.json()}")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["email"] == "test_register@example.com"

def test_duplicate_registration():
    """Test that registering with same email fails"""
    user_data = {
        "email": "test_dup@example.com",
        "password": "securepassword123"
    }

    # First registration should succeed
    response1 = client.post("/auth/register", json=user_data)
    assert response1.status_code == 200

    # Second registration with same email should fail
    response2 = client.post("/auth/register", json=user_data)
    print(f"Duplicate register response: {response2.status_code}, {response2.json()}")
    assert response2.status_code == 409  # Conflict

def test_login_nonexistent_user():
    """Test login with nonexistent user"""
    login_data = {
        "email": "nonexistent@example.com",
        "password": "wrongpassword"
    }
    response = client.post("/auth/login", json=login_data)
    print(f"Login nonexistent user response: {response.status_code}, {response.json()}")
    assert response.status_code == 401  # Unauthorized

if __name__ == "__main__":
    test_register_user_success()
    test_duplicate_registration()
    test_login_nonexistent_user()
    print("Database-enabled tests completed successfully!")