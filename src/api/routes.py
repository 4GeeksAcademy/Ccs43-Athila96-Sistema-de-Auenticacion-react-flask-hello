"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200




# ENDPOINT PARA CREAR USURIO

@api.route('/singup', methods=["POST"])
def create_user():

    body =  request.json
    email = body.get("email")
    password = body.get("password")
    
    user_exist = User.query.filter_by(email=email).one_or_none()
    if user_exist is not None:
        return jsonify({
            "message": "User already exists"
        }), 400
    
    new_user = User(
        email = email,
        password = password
    )

    try:
        db.session.add(new_user)
        db.session.commit()
    except Exception as error:
        db.session.rollback()
        return jsonify({
            "message": "an internal error occurred",
            "error": error.args
        }), 500
    
    return jsonify({}), 201


# ENDPOINT PARA EL LOGIN (GENERAR EL TOKEN)

@api.route('/login', methods=["POST"])
def handle_login():
    body =  request.json
    email = body.get("email")
    password = body.get("password")

    if email is None or password is None:
        return jsonify({
            "message": "email and password required"
        }), 400
    
    user = User.query.filter_by(email=email).one_or_none()

    if user is None:
        return jsonify({
            "message": "Invalid credential"
        }), 400
    
    password_valid = password == user.password

    if not password_valid:
        return jsonify({
           "message": "email and password required"
        }), 400
    
    access_token = create_access_token(identity=user.id)

    return jsonify({
        "token": access_token 
    }), 201


# 

@api.route('/private', methods=["GET"])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    user = User.query.get(current_user)
    return jsonify(user.serialize()), 200
