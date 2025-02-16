from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

client = TestClient(app)

# Sample user data
user_data = {
    "name": "John Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "phone": "1234567890",
    "houses": []
}

def test_create_user():
    """Test creating a user"""
    response = client.post("/users", json=user_data)
    assert response.status_code == 200
    assert "user_id" in response.json()
    assert response.json()["name"] == user_data["name"]

def test_get_user():
    """Test retrieving a user by ID"""
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json()["user_id"] == 1

def test_update_user():
    """Test updating user details"""
    updated_data = {
        "name": "John Updated",
        "username": "johnupdated",
        "email": "johnupdated@example.com",
        "phone": "0987654321",
        "houses": []
    }
    response = client.put("/users/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"

def test_assign_house_to_user():
    response = client.post("/users/1/houses/101")
    assert response.status_code == 200
    assert response.json()["message"] == "House 101 assigned to User 1"

def test_get_houses_from_user():
    response = client.post("/users/1/houses")
    assert response.status_code == 200
    assert 101 in response.json()  # Ensure the house was assigned

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json()["message"] == "User 1 deleted successfully"

    # Verify user no longer exists
    response = client.get("/users/1")
    assert response.status_code == 404  # User should be gone


