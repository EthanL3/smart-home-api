from flask import Blueprint, request, jsonify
from models.house import House
from models.room import Room
from models.device import Device

house_bp = Blueprint('house', __name__)

houses = {}

# House CRUD
@house_bp.route('', methods=['POST'])
def create_house():
    data = request.json
    return create_house_stub(data['address'], data['city'], data['state'], data['zipcode'], data['sqft'])

@house_bp.route('/<int:house_id>', methods=['GET'])
def get_house(house_id):
    return get_house_stub(house_id)

@house_bp.route('/<int:house_id>', methods=['PUT'])
def update_house(house_id):
    data = request.json
    return update_house_stub(house_id, data)

@house_bp.route('/<int:house_id>', methods=['DELETE'])
def delete_house(house_id):
    return delete_house_stub(house_id)


# Room CRUD
@house_bp.route('/<int:house_id>/rooms', methods=['POST'])
def add_room(house_id):
    data = request.json
    return add_room_stub(house_id, data)
    
@house_bp.route('/<int:house_id>/rooms/<int:room_id>', methods=['GET'])
def get_room(house_id, room_id):
    data = request.json
    return get_room_stub(house_id, room_id)

@house_bp.route('/<int:house_id>/rooms/<int:room_id>', methods=['PUT'])
def update_room(house_id, room_id):
    data = request.json
    return update_room_stub(house_id, room_id, data)

@house_bp.route('/<int:house_id>/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(house_id, room_id):
    return delete_room_stub(house_id, room_id)


# Device CRUD
@house_bp.route('/<int:house_id>/rooms/<int:room_id>/devices', methods=['POST'])
def add_device(house_id, room_id):
    data = request.json
    return add_device_stub(house_id, room_id, data)

@house_bp.route('/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['GET'])
def get_device(house_id, room_id, device_id):
    return get_device_stub(house_id, room_id, device_id)

@house_bp.route('/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['PUT'])
def update_device(house_id, room_id, device_id):
    data = request.json
    return update_device_stub(house_id, room_id, device_id, data)

@house_bp.route('/<int:house_id>/rooms/<int:room_id>/devices/<int:device_id>', methods=['DELETE'])
def delete_device(house_id, room_id, device_id):
    return delete_device_stub(house_id, room_id, device_id)


# House Stubs
def create_house_stub(data):
    house_id = len(houses) + 1

    for house in houses.values():
        if house.address == data['address'] and house.city == data['city'] and house.state == data['state'] and house.zipcode == data['zipcode']:
            return jsonify({'error': 'House already exists'}), 400
    
    new_house = House(house_id, data['address'], data['city'], data['state'], data['zipcode'], data['sqft'])
    houses[house_id] = new_house
    return jsonify(houses[house_id]), 201

def get_house_stub(house_id):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    return jsonify(house), 200

def update_house_stub(house_id, data):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    houses[house_id].update(data)
    return jsonify(houses[house_id]), 200

def delete_house_stub(house_id):
    if house_id in houses:
        del houses[house_id]
        return jsonify({'message': 'House deleted'}), 204
    return jsonify({'error': 'House not found'}), 404

# Room Stubs
def add_room_stub(house_id, data):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room_id = len(house.rooms) + 1
    room = Room(room_id, data['name'], data['sqft'])
    house.add_room(room)
    return jsonify(house), 201

def get_room_stub(house_id, room_id):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    return jsonify(room), 200

def update_room_stub(house_id, room_id, data):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    house.rooms[room_id].update(data)
    return jsonify(house.rooms[room_id]), 200

def delete_room_stub(house_id, room_id):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    if room_id in house.rooms:
        del house.rooms[room_id]
        return jsonify({'message': 'Room deleted'}), 204
    return jsonify({'error': 'Room not found'}), 404


# Device Stubs
def add_device_stub(house_id, room_id, data):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    device_id = len(room.devices) + 1
    device = Device(device_id, data['name'], data['type'], data['status'])
    room.add_device(device)
    return jsonify(room), 201

def get_device_stub(house_id, room_id, device_id):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    device = room.devices.get(device_id)
    if not device:
        return jsonify({'error': 'Device not found'}), 404
    return jsonify(device), 200

def update_device_stub(house_id, room_id, device_id, data):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    device = room.devices.get(device_id)
    if not device:
        return jsonify({'error': 'Device not found'}), 404
    room.devices[device_id].update(data)
    return jsonify(room.devices[device_id]), 200

def delete_device_stub(house_id, room_id, device_id):
    house = houses.get(house_id)
    if not house:
        return jsonify({'error': 'House not found'}), 404
    room = house.rooms.get(room_id)
    if not room:
        return jsonify({'error': 'Room not found'}), 404
    if device_id in room.devices:
        del room.devices[device_id]
        return jsonify({'message': 'Device deleted'}), 204
    return jsonify({'error': 'Device not found'}), 404
