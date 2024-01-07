import json
from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS
from api.organization.handler.RequestArchiveOrganization import RequestArchiveOrganization
from api.organization.handler.RequestDeleteOrganization import RequestDeleteOrganization

from api.user.handler.HandleCreateUser import HandleCreateUser
from api.user.handler.HandleGetUser import HandleGetUser
from api.user.handler.HandleLogin import HandleLogin
from api.user.handler.RequestArchiveUser import RequestArchiveUser
from api.user.handler.RequestCreateUser import RequestCreateUser
from api.user.handler.RequestDeleteUser import RequestDeleteUser
from api.user.handler.RequestGetUserById import RequestGetUserById
from api.user.handler.RequestUpdateUser import RequestUpdateUser


user_api = Blueprint('user_api', __name__)
CORS(user_api)

@user_api.route('/api/user', methods=['POST', 'OPTIONS'])
def create_user():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    data = json.loads(request.data)
    #handler = HandleCreateUser(data)
    #response = handler.do_process()

    api_request = RequestCreateUser(data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/<user_id>', methods=["GET"])
def get_user(user_id):

    # handler = HandleGetUser(user_id)
    # user = handler.do_process()

    api_request = RequestGetUserById(user_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/<user_id>', methods=["PATCH"])
def update_user(user_id):
    data = json.loads(request.data)
    # handler = HandleUpdateUser(data, user_id)
    # response = handler.do_process()

    api_request = RequestUpdateUser(user_id, data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/archive/<user_id>', methods=["DELETE"])
def archive_user(user_id):

    # handler = HandleArchiveUser(data, user_id)
    # response = handler.do_process()

    api_request = RequestArchiveUser(user_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
    

@user_api.route('/api/user/<user_id>', methods=["DELETE"])
def delete_user(user_id):
    # handler = HandleDeleteUser(user_id)
    # response = handler.do_process()

    api_request = RequestDeleteUser(user_id)
    response = api_request.do_process()

    response = make_response(response, 200)
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

