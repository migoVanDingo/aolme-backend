from flask import Blueprint, make_response, request
from flask_cors import CORS


config_api = Blueprint('config_api', __name__)
CORS(config_api)

@config_api.route('/api/config', methods=['POST', 'OPTIONS'])
def create_config():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    print("data: {}".format(request.data))
    
    # ENDPOINT LOGIC
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@config_api.route('/api/config', methods=['GET'])
def get_configs():
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@config_api.route('/api/config/<config_id>', methods=['GET'])
def get_config(config_id):
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@config_api.route('/api/config/<config_id>', methods=['PUT'])
def update_config(config_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@config_api.route('/api/config/<config_id>', methods=['DELETE'])
def delete_config(config_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@config_api.route('/api/config/archive/<config_id>', methods=['DELETE'])
def archive_config(config_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
