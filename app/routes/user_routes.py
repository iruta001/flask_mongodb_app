from flask import Blueprint, request, jsonify
from app.utils.db import db
from app.models.user_model import Entry 
from bson import ObjectId

user_api = Blueprint('user_api', __name__)

def serialize_user(user):
    if isinstance(user, dict):
        user['_id'] = str(user['_id'])
        return user 
    else:
        raise ValueError("Expected dictionary but got a different data type")

@user_api.route('/', methods = ['GET'])
def get_users():
    try:
        users = list(db.users.find())
        serialized_users = [serialize_user(user) for user in users]
        return jsonify (users)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_api.route('/<id>', methods = ['GET'])
def get_user(id):
    try:
        user = db.users.find_one({"_id": ObjectId(id)})
        serialize_data = serialize_user(user) if user else None
        return jsonify(serialize_data) if serialize_user else ({"Message": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_api.route('/', methods = ['POST'])
def create_user():
    try:
        data = request.json
        if not data or 'name' not in data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'data does not exist'}), 400
        
        user_id = db.users.insert_one(data).inserted_id
        return jsonify({'message': 'user created', 'user_id': str(user_id)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_api.route('/<id>', methods = ['PUT'])
def update_user(id):
    try:
        data = request.json
        result = db.users.update_one({"_id": ObjectId(id)}, {"$set": data})
        if result.matched_count > 0:
            return jsonify({"message": "User Updated"})
        else:
            return jsonify({'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_api.route('/<id>', methods = ['DELETE'])
def del_user(id):
    try:
        result = db.users.delete_one({'_id': ObjectId(id)})
        if result.deleted_count > 0:
            return jsonify({"Message": "User Deleted"})
        else:
            return jsonify({"Message": "User not found"}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
