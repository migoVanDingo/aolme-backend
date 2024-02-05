import json
from flask import Blueprint, make_response, request
from flask_cors import CORS
from api.entity_user.handler.RequestArchiveEntityUser import RequestArchiveEntityUser
from api.entity_user.handler.RequestDeleteEntityUser import RequestDeleteEntityUser
from api.entity_user.handler.RequestGetEntityListByUserId import RequestGetEntityListByUserId
from api.entity_user.handler.RequestGetUserListByEntityId import RequestGetUserListByEntityId

from api.entity_user.handler.RequestInsertEntityUser import RequestInsertEntityUser
from api.entity_user.handler.RequestUpdateEntityUser import RequestUpdateEntityUser


entity_user_api = Blueprint('entity_user_api', __name__)
CORS(entity_user_api)

@entity_user_api.route('/api/entity-user', methods=['POST', 'OPTIONS'])
def insert_entity_user():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    print("data: {}".format(request.data))
    
    # ENDPOINT LOGIC
    api_request = RequestInsertEntityUser()
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@entity_user_api.route('/api/entity-user/entity/<entity_id>', methods=['GET'])
def get_user_list_by_entity_id(entity_id):
    try:
        # ENDPOINT LOGIC
        api_request = RequestGetUserListByEntityId(entity_id)
        response = api_request.do_process()
    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        print(str(e))
        return "Error: " + str(e), 404

@entity_user_api.route('/api/entity-user/user/<user_id>', methods=['GET'])
def get_entity_list_by_user_id(user_id):
            
         
            # ENDPOINT LOGIC
            api_request = RequestGetEntityListByUserId(user_id)
            response = api_request.do_process()
        
            response = make_response(response, 200)
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Content-Type'] = '*'
            return response

@entity_user_api.route('/api/entity-user/entity/<entity_id>', methods=['GET'])
def get_user_list_by_entity(entity_id):
    try:
        # ENDPOINT LOGIC
        api_request = RequestGetUserListByEntityId(entity_id)
        response = api_request.do_process()
    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        print(str(e))
        return "Error: " + str(e), 404

@entity_user_api.route('/api/entity-user', methods=['PATCH', 'OPTIONS'])
def update_entity_user():
    
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    data = json.loads(request.data)

    # ENDPOINT LOGIC
    api_request = RequestUpdateEntityUser(data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@entity_user_api.route('/api/entity-user/<entity_user_id>', methods=['DELETE'])
def delete_entity_user(entity_user_id):
        
        # ENDPOINT LOGIC
        api_request = RequestDeleteEntityUser(entity_user_id)
        response = api_request.do_process()
    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

@entity_user_api.route('/api/entity-user/<entity_user_id>', methods=['PATCH', 'OPTIONS'])
def archive_entity_user(entity_user_id):

    # ENDPOINT LOGIC
    api_request = RequestArchiveEntityUser(entity_user_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

    