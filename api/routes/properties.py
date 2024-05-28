from flask import Blueprint, request, jsonify
from app.models import Property, User
from app import db
from flask_jwt_extended import jwt_required, get_jwt_identity

properties_bp = Blueprint('properties_bp', __name__)

@properties_bp.route('/', methods=['POST'])
@jwt_required()
def create_property():
    data = request.get_json()
    current_user = get_jwt_identity()
    user = User.query.filter_by(username=current_user['username']).first()
    new_property = Property(
        title=data['title'],
        description=data['description'],
        price=data['price'],
        owner=user
    )
    db.session.add(new_property)
    db.session.commit()
    return jsonify({'message': 'Property created successfully'}), 201

@properties_bp.route('/', methods=['GET'])
def get_properties():
    properties = Property.query.all()
    properties_list = [
        {
            'id': prop.id,
            'title': prop.title,
            'description': prop.description,
            'price': prop.price,
            'owner': prop.owner.username
        } for prop in properties
    ]
    return jsonify(properties_list), 200

