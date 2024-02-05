from flask import Blueprint, make_response, request
from flask_cors import CORS


module_api = Blueprint('module_api', __name__)
CORS(module_api)

@module_api.route('/api/module', methods=['POST', 'OPTIONS'])
def create_module():
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



@module_api.route('/api/module', methods=['GET'])
def get_modules():
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@module_api.route('/api/module/<module_id>', methods=['GET'])
def get_module(module_id):
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@module_api.route('/api/module/<module_id>', methods=['PUT'])
def update_module(module_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@module_api.route('/api/module/<module_id>', methods=['DELETE'])
def delete_module(module_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@module_api.route('/api/module/archive/<module_id>', methods=['DELETE'])
def archive_module(module_id):
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
