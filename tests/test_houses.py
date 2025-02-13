def test_create_house(client):
    response = client.post('/houses', json={"address": "123 Street", "city": "Anytown"})
    assert response.status_code == 201
    assert response.json['address'] == "123 Street"

def test_get_house(client):
    response = client.get('/houses/1')
    assert response.status_code == 200
    assert 'address' in response.json
