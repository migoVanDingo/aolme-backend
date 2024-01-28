import json
from flask import Blueprint, make_response, request
from flask_cors import CORS
from api.repository.handler.RequestArchiveRepo import RequestArchiveRepo

from api.repository.handler.RequestCreateRepo import RequestCreateRepository
from api.repository.handler.RequestDeleteRepo import RequestDeleteRepo
from api.repository.handler.RequestGetRepoByEntity import RequestGetRepoByEntity
from api.repository.handler.RequestGetRepoById import RequestGetRepoById
from api.repository.handler.RequestGetRepoByOwner import RequestGetRepoByOwner
from api.repository.handler.RequestUpdateRepo import RequestUpdateRepo


repository_api = Blueprint('repository_api', __name__)
CORS(repository_api)

@repository_api.route('/api/repository', methods=['POST', 'OPTIONS'])
def create_repository():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    # ENDPOINT LOGIC
    api_request = RequestCreateRepository(json.loads(request.data))
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@repository_api.route('/api/repository/<repo_id>', methods=['GET'])
def get_repository_by_id(repo_id):
        
    # ENDPOINT LOGIC
    api_request = RequestGetRepoById(repo_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response



@repository_api.route('/api/repository/owner/<owner_id>', methods=['GET'])
def get_repository_list_by_owner_id(owner_id):
            
    # ENDPOINT LOGIC
    api_request = RequestGetRepoByOwner(owner_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@repository_api.route('/api/repository/entity/<entity_id>', methods=['GET'])
def get_repository_list_by_entity_id(entity_id):
                    
    # ENDPOINT LOGIC
    api_request = RequestGetRepoByEntity(entity_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response 


@repository_api.route('/api/repository/<repo_id>', methods=['PATCH', 'OPTIONS'])
def update_repository_by_id(repo_id):
    
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    # ENDPOINT LOGIC
    api_request = RequestUpdateRepo(repo_id, json.loads(request.data))
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@repository_api.route('/api/repository/<repo_id>', methods=['DELETE', 'OPTIONS'])
def delete_repository_by_id(repo_id):
    
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    # ENDPOINT LOGIC
    api_request = RequestDeleteRepo(repo_id)
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


@repository_api.route('/api/repository/archive/<repo_id>', methods=['DELETE', 'OPTIONS'])
def archive_repository_by_id(repo_id):
    
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    # ENDPOINT LOGIC
    api_request = RequestArchiveRepo(repo_id)
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response


