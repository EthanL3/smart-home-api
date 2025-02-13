def test_create_user(client):
    response = client.post('/users', json={"name": "Alice", "email": "alice@example.com", "phone": "123-456"})
    assert response.status_code == 201
    assert response.json['name'] == "Alice"

def test_get_user(client):
    response = client.get('/users/1')
    assert response.status_code == 200
    assert 'name' in response.json
