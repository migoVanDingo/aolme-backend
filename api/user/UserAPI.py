import json
from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS

from api.user.handler.HandleCreateUser import HandleCreateUser
from api.user.handler.HandleGetUser import HandleGetUser
from api.user.handler.HandleLogin import HandleLogin


user_api = Blueprint('user_api', __name__)
CORS(user_api)

@user_api.route('/api/user', methods=['POST', 'OPTIONS'])
def handle_create_user():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    data = json.loads(request.data)
    handler = HandleCreateUser(data)
    response = handler.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/<user_id>', methods=["GET"])
def get_user(user_id):

    handler = HandleGetUser(user_id)
    user = handler.do_process()

    response = make_response(user, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/login', methods=["POST", "OPTIONS"])
def login():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    data = json.loads(request.data)
    handler = HandleLogin(data)
    response = handler.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response