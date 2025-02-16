from fastapi.testclient import TestClient
from app import app  # Import your FastAPI app

client = TestClient(app)

device_data = {
    "name": "Smart Light",
    "type": "Light",
    "status": "On"
}

# 🔹 DEVICES TESTS
def test_create_device():
    response = client.post("/devices/", json=device_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Smart Light"

def test_get_device():
    response = client.get("/devices/1")
    assert response.status_code == 200
    assert response.json()["device_id"] == 1

def test_update_device():
    updated_data = {
        "name": "Updated Device",
        "type": "Light",
        "status": "On"
    }
    response = client.put("/devices/1", json=updated_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Updated Device"

def test_delete_device():
    response = client.delete("/devices/1")
    assert response.status_code == 200
    assert response.json()["message"] == "Device 1 deleted successfully"