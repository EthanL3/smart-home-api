import pytest
from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

client = TestClient(app)

house_data = {
    "address": "123 Main St",
    "city": "Boston",
    "state": "MA",
    "zipcode": "02215",
    "sqft": "2000",
    "rooms": []
}

# 🔹 HOUSES TESTS
def test_create_house():
    response = client.post("/houses/", json=house_data)
    assert response.status_code == 200
    assert "house_id" in response.json()
    assert response.json()["address"] == "123 Main St"

def test_get_house():
    response = client.get("/houses/1")
    assert response.status_code == 200
    assert response.json()["house_id"] == 1

def test_update_house():
    updated_data = {
        "address": "456 Elm St",
        "city": "Updated City",
        "state": "Updated State",
        "zipcode": "12345",
        "sqft": 3000,
        "rooms": []
    }
    response = client.put("/houses/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["address"] == "456 Elm St"

def test_assign_room_to_house():
    response = client.post("/houses/1/rooms/101")
    assert response.status_code == 200
    assert response.json()["message"] == "Room 101 assigned to House 1"

def test_get_rooms_from_house():
    response = client.get("/houses/1/rooms")
    assert response.status_code == 200
    assert 101 in response.json()

def test_delete_house():
    response = client.delete("/houses/1")
    assert response.status_code == 200
    assert response.json()["message"] == "House 1 deleted successfully"

    # Verify house no longer exists
    response = client.get("/houses/1")
    assert response.status_code == 404