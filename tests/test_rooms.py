from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

client = TestClient(app)

room_data = {
    "name": "Living Room",
    "area": 200,
    "devices": []
}

# 🔹 ROOMS TESTS
def test_create_room():
    response = client.post("/rooms/", json=room_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Living Room"

def test_get_room():
    response = client.get("/rooms/1")
    assert response.status_code == 200
    assert response.json()["room_id"] == 1

def test_update_room():
    updated_data = {
        "name": "Updated Room",
        "area": 300,
        "devices": []
    }
    response = client.put("/rooms/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Room"

def test_assign_device_to_room():
    response = client.post("/rooms/1/devices/101")
    assert response.status_code == 200
    assert response.json()["message"] == "Device 101 assigned to Room 1"

def test_get_devices_from_room():
    response = client.post("/rooms/1/devices")
    assert response.status_code == 200
    assert 101 in response.json()

def test_delete_room():
    response = client.delete("/rooms/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Room 1 deleted successfully"