

from flask import jsonify, request, abort
from models import storage
from models.user import User
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """
    Retrieves the list of all User objects.
    """
    users = [user.to_dict() for user in storage.all(User).values()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """
    Retrieves a User object by ID.
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """
    Deletes a User object by ID.
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({})

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """
    Creates a new User object.
    """
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    if 'email' not in data:
        abort(400, description="Missing email")
    if 'password' not in data:
        abort(400, description="Missing password")
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """
    Updates a User object by ID.
    """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    if not request.json:
        abort(400, description="Not a JSON")
    data = request.get_json()
    for key, value in data.items():
        if key not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())
