def test_add_device(client):
    response = client.post('/houses/1/rooms/1/devices', json={"name": "Smart Light", "type": "Light"})
    assert response.status_code == 201
    assert response.json['name'] == "Smart Light"
