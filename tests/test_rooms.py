def test_add_room(client):
    response = client.post('/houses/1/rooms', json={"name": "Living Room"})
    assert response.status_code == 201
    assert response.json['name'] == "Living Room"
