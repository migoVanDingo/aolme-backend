import json
from flask import Blueprint, current_app, make_response, request
from flask_cors import CORS
from api.repository.handler.RequestGetRepoStages import RequestGetRepoStages
from api.repository.handler.RequestGetGithubRepoContents import RequestGetGithubRepoContents
from api.repository.handler.RequestSyncGithubRepo import RequestSyncGithubRepo
from api.repository.handler.RequestCloneRepo import RequestCloneRepo
from api.repository.handler.RequestAddRepoItem import RequestAddRepoItem
from api.repository.handler.RequestArchiveRepo import RequestArchiveRepo

from api.repository.handler.RequestCreateRepo import RequestCreateRepo
from api.repository.handler.RequestDeleteRepo import RequestDeleteRepo
from api.repository.handler.RequestGetRepoByEntity import RequestGetRepoByEntity
from api.repository.handler.RequestGetRepoById import RequestGetRepoById
from api.repository.handler.RequestGetRepoByOwner import RequestGetRepoByOwner
from api.repository.handler.RequestGetRepoItemList import RequestGetRepoItemList
from api.repository.handler.RequestUpdateRepo import RequestUpdateRepo
from api.repository.handler.RequestCheckAndUpdateRepoItem import RequestCheckAndUpdateRepoItem


repository_api = Blueprint('repository_api', __name__)
CORS(repository_api)

@repository_api.route('/api/repository', methods=['POST', 'OPTIONS'])
def create_repository():
    
    # ENDPOINT LOGIC
    api_request = RequestCreateRepo(json.loads(request.data))
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


@repository_api.route('/api/repository/<repo_id>/items', methods=['GET'])
def get_repository_items_by_id(repo_id):
        
        # ENDPOINT LOGIC
        api_request = RequestGetRepoItemList(repo_id)
        response = api_request.do_process()
    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response



@repository_api.route('/api/repository/<repo_id>', methods=['PATCH', 'OPTIONS'])
def update_repository_by_id(repo_id):
    
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
    
    # ENDPOINT LOGIC
    api_request = RequestArchiveRepo(repo_id)
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/<repo_id>/item', methods=['POST', 'OPTIONS'])
def add_repo_item(repo_id):

    
    # ENDPOINT LOGIC
    api_request = RequestAddRepoItem(repo_id, json.loads(request.data))
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/<repo_id>/item/update', methods=['POST', 'OPTIONS'])
def update_repo_item(repo_id):
    
    data = json.loads(request.data)
    
    # ENDPOINT LOGIC
    api_request = RequestCheckAndUpdateRepoItem(data, repo_id)
    response = api_request.do_process()

    
    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/clone', methods=['POST', 'OPTIONS'])
def clone_repo():
    data = json.loads(request.data)

    api_request = RequestCloneRepo(data)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/<repo_id>/sync', methods=['GET'])
def sync_repo(repo_id):

    api_request = RequestSyncGithubRepo(repo_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/<repo_id>/contents', methods=['GET'])
def get_repo_contents(repo_id):
    
    api_request = RequestGetGithubRepoContents(repo_id)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response

@repository_api.route('/api/repository/stages', methods=['GET'])
def get_repo_stages():


    path = request.args.get('path')
    current_app.logger.debug(f"get_repo_stages :: path: {path}")
    
    api_request = RequestGetRepoStages(path)
    response = api_request.do_process()

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
