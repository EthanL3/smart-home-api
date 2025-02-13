from flask import Blueprint, request, jsonify
from models.user import User

user_bp = Blueprint('user', __name__)

users = {}

# User CRUD
@user_bp.route('', methods=['POST'])
def create_user():
    data = request.json
    return create_user_stub(data['name'], data['username'], data['email'], data['phone'])

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_stub(user_id)

@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    return update_user_stub(user_id, data)

@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_stub(user_id)

# User CRUD Stubs
def create_user_stub(name, username, email, phone):
    user_id = len(users) + 1
    for user in users.values():
        if user.username == username:
            return jsonify({'error': 'Username already exists'}), 400
        if user.email == email:
            return jsonify({'error': 'Email already exists'}), 400
    new_user = User(user_id, name, username, email, phone)
    users[user_id] = new_user
    return jsonify(new_user.to_dict()), 201


def get_user_stub(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user), 200

def update_user_stub(user_id, data):
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    users[user_id].update(data)
    return jsonify(users[user_id]), 200

def delete_user_stub(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({'message': 'User deleted'}), 204
    return jsonify({'error': 'User not found'}), 404

