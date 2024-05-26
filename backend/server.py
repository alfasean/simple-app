from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid

app = Flask(__name__)
CORS(app)

users = []

@app.route("/account", methods=["POST"]) 
def create_account():
    data = request.get_json()
    name = data.get("name")
    password = data.get("password")

    user_id = str(uuid.uuid4())

    new_user = {'id' : user_id, 'name' : name, 'password' : password}
    users.append(new_user)

    return jsonify({'message': 'User created successfully!', 'users' : new_user}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    
    for user in users:
        if user['name'] == name and user['password'] == password:
            return jsonify({'message': 'Login Success', 'user': user}), 200
    
    return jsonify({'error': 'name atau password salah'}), 401

@app.route("/account/<user_id>", methods=["GET"]) 
def get_account(user_id):
    for user in users:
        if user['id'] == user_id:
            return jsonify(user), 200
        
    return jsonify({'message': 'User not found!'}), 404

@app.route('/account/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json()
    name = data.get('name')
    password = data.get('password')
    
    for user in users:
        if user['id'] == user_id:
            if name:
                user['name'] = name
            if password:
                user['password'] = password
            return jsonify({'message': 'Pengguna berhasil diperbarui', 'user': user}), 200
    
    return jsonify({'error': 'Pengguna tidak ditemukan'}), 404

@app.route("/account/<user_id>", methods=["DELETE"])
def delete_account(user_id):
    for user in users:
        if user['id'] == user_id:
            users.remove(user)
            return jsonify({'message': 'Pengguna berhasil dihapus!'}), 200
    
    return jsonify({'error': 'Pengguna tidak ditemukan'}), 404

if __name__ == "__main__":
    app.run(debug=True)