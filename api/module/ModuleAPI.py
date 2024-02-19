import json
from flask import Blueprint, make_response, request
from flask_cors import CORS
from api.module.handler.RequestArchiveModule import RequestArchiveModule

from api.module.handler.RequestCreateModule import RequestCreateModule
from api.module.handler.RequestDeleteModule import RequestDeleteModule
from api.module.handler.RequestGetModuleById import RequestGetModuleById
from api.module.handler.RequestGetModuleListByEntity import RequestGetModuleListByEntity
from api.module.handler.RequestGetModuleListByUser import RequestGetModuleListByUser
from api.module.handler.RequestGetModuleListPublic import RequestGetModuleListPublic
from api.module.handler.RequestUpdateModule import RequestUpdateModule


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
    
    repo_id = request.args.get('repo_id')

    print("repoId: " + repo_id)
    
    files = request.files.getlist('file')
    data = request.form
    
    # ENDPOINT LOGIC
    api_request = RequestCreateModule(data, files, repo_id)
    response = api_request.do_process()
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module', methods=['GET'])
def get_modules():
    
    api_request = RequestGetModuleListPublic()
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module/<module_id>', methods=['GET'])
def get_module(module_id):

    api_request = RequestGetModuleById(module_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module/entity/<entity_id>', methods=['GET'])
def get_module_list_by_entity(entity_id):

    api_request = RequestGetModuleListByEntity(entity_id) 
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module/user/<user_id>', methods=['GET'])
def get_module_list_by_user(user_id):

    api_request = RequestGetModuleListByUser(user_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module/<module_id>', methods=['PUT'])
def update_module(module_id):

    api_request = RequestUpdateModule(module_id, json.loads(request.data))
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@module_api.route('/api/module/<module_id>', methods=['DELETE'])
def delete_module(module_id):

    api_request = RequestDeleteModule(module_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@module_api.route('/api/module/archive/<module_id>', methods=['DELETE'])
def archive_module(module_id):

    api_request = RequestArchiveModule(module_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
