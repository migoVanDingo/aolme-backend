import json
from flask import Blueprint, make_response, request
from flask_cors import CORS

from api.config.handler.RequestCreateConfig import RequestCreateConfig
from api.config.handler.RequestDeleteConfig import RequestDeleteConfig
from api.config.handler.RequestGetConfigById import RequestGetConfigById
from api.config.handler.RequestGetConfigListByEntity import RequestGetConfigListByEntity
from api.config.handler.RequestGetConfigListByUser import RequestGetConfigListByUser
from api.config.handler.RequestGetConfigListPublic import RequestGetConfigListPublic
from api.config.handler.RequestUpdateConfig import RequestUpdateConfig


config_api = Blueprint('config_api', __name__)
CORS(config_api)

@config_api.route('/api/config', methods=['POST', 'OPTIONS'])
def create_config():
    repo_id = request.args.get('repo_id')


    files = request.files.getlist('file')
    data = request.form

    
    # ENDPOINT LOGIC
    api_request = RequestCreateConfig(data, files, repo_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@config_api.route('/api/config', methods=['GET'])
def get_configs():
    
    api_request = RequestGetConfigListPublic()
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@config_api.route('/api/config/<config_id>', methods=['GET'])
def get_config(config_id):
    
    api_request = RequestGetConfigById(config_id)
    response = api_request.do_process()
    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@config_api.route('/api/config/entity/<entity_id>', methods=['GET'])
def get_config_by_entity(entity_id):
        
        api_request = RequestGetConfigListByEntity(entity_id)
        response = api_request.do_process()
        
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response


@config_api.route('/api/config/user/<user_id>', methods=['GET'])
def get_config_by_user(user_id):
        
        api_request = RequestGetConfigListByUser(user_id)
        response = api_request.do_process()
        
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response


@config_api.route('/api/config/<config_id>', methods=['PUT'])
def update_config(config_id):

    api_request = RequestUpdateConfig(config_id, json.loads(request.data))
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@config_api.route('/api/config/<config_id>', methods=['DELETE'])
def delete_config(config_id):

    api_request = RequestDeleteConfig(config_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@config_api.route('/api/config/archive/<config_id>', methods=['DELETE'])
def archive_config(config_id):

    api_request = RequestDeleteConfig(config_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
