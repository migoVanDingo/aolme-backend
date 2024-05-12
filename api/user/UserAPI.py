import json
from logging import Logger
from flask import Blueprint, jsonify, make_response, request, current_app
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
from app.logger.AppLogger import AppLogger


user_api = Blueprint('user_api', __name__)
CORS(user_api)

@user_api.route('/api/user', methods=['POST', 'OPTIONS'])
def create_user():
    
    

    args = request.args
    if "entity_id" in args:
        entity_id = args["entity_id"]
    
    if "entity_type" in args:
        entity_type = args["entity_type"]

    print("request.data: {}".format(json.loads(request.data)))
    data = json.loads(request.data)
    
    api_request = RequestCreateUser(data, entity_id, entity_type)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@user_api.route('/api/user/<user_id>', methods=["GET"])
def get_user(user_id):

    current_app.logger.info("Get User ID: {}".format(user_id))

    handler = HandleGetUser(user_id)
    user = handler.do_process()

    # api_request = RequestGetUserById(user_id)
    # response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/<user_id>', methods=["PATCH"])
def update_user(user_id):
    data = json.loads(request.data)
    print("\nEdit User Data =======>>>>>>> {}\n\n".format(data))
    #handler = RequestUpdateUser(data, user_id)
    #response = handler.do_process()

    api_request = RequestUpdateUser(user_id, data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@user_api.route('/api/user/archive/<user_id>', methods=["DELETE"])
def archive_user(user_id):

    handler = HandleArchiveUser(data, user_id)
    response = handler.do_process()

    # api_request = RequestArchiveUser(user_id)
    # response = api_request.do_process()

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
    
    data = json.loads(request.data)
    handler = HandleLogin(data)
    response = handler.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


