from datetime import datetime
import json
from flask import Blueprint, current_app, jsonify, make_response, request
from flask_cors import CORS
from api.directory_tree.handler.ReadProjectFolder import ReadProjectFolder

from api.directory_tree.handler.ReadProjectRoot import ReadProjectRoot
from api.directory_tree.handler.ReadRepoDirectory import ReadRepoDirectory
from api.directory_tree.handler.RequestCreateOrganizationDirectory import RequestCreateOrganizationDirectory
from api.directory_tree.handler.RequestCreateProjectDirectory import RequestCreateProjectDirectory
from api.directory_tree.handler.RequestCreateUserDirectory import RequestCreateUserDirectory
from api.directory_tree.handler.RequestGetFolderItems import RequestGetFolderItems
from utility.Directory import Directory


directory_tree_api = Blueprint('directory_tree_api', __name__)
CORS(directory_tree_api)

@directory_tree_api.route('/api/directory/repo/<repo_id>', methods=['GET'])
def get_project_root(repo_id):
   try:
        entity_id = request.args.get('entity_id')
        directory_read_request = ReadRepoDirectory(repo_id, entity_id)
        dir_read_res = directory_read_request.do_process()

        if dir_read_res is not None:
            res = dir_read_res
        else:
            res = 'fail'

        response = make_response(res, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
   except Exception as e:
        current_app.logger.error("DirectoryTreeAPI -- get_project_root() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_project_root:: " + str(e), 404
   

@directory_tree_api.route('/api/directory/entity/<entity_id>/folder/<folder_name>/owner/<owner_id>/repo/<repo_id>', methods=['GET'])
def get_directory_items(entity_id, folder_name, owner_id, repo_id):
    try:
 
        api_request = RequestGetFolderItems(entity_id, folder_name, owner_id, repo_id)
        response = api_request.do_process()

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
       
    except Exception as e:
        current_app.logger.error("DirectoryTreeAPI -- get_directory_items() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_directory_items:: " + str(e), 404

    

@directory_tree_api.route('/api/directory/entity/<entity_id>/folder', methods=['GET'])
def get_folder_items(entity_id):
    try:
        rawrgs = request.args.get('fa')
        
        


        api_request = ReadProjectFolder(entity_id, [rawrgs])
        response = api_request.do_process()
        
        
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
       
    except Exception as e:
        current_app.logger.error("DirectoryTreeAPI -- get_folder_items() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_folder_items:: " + str(e), 404




@directory_tree_api.route('/api/directory/project/<project_id>/new', methods=['POST', 'OPTIONS'])
def create_directory(project_id):

    try:

        data = json.loads(request.data)
    
        response = Directory.create_directory(project_id, data['name'])

        response = make_response(response, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        # Handle any errors that occur while running the commands
        current_app.logger.error("DirectoryTreeAPI -- create_directory() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::create_directory:: " + str(e), 404
    
    
@directory_tree_api.route('/api/directory/organization/<org_id>/project/<project_id>', methods=['POST', 'OPTIONS'])
def create_project_directory(org_id, project_id):
    
    try:
        api_request = RequestCreateProjectDirectory(org_id, project_id)
        response = api_request.do_process()

        response = make_response(response, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        # Handle any errors that occur while running the commands
        current_app.logger.error("DirectoryTreeAPI -- create_project_directory() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::create_project_directory:: " + str(e), 404


@directory_tree_api.route('/api/directory/organization/<org_id>', methods=['POST', 'OPTIONS'])
def create_organization_directory(org_id):
    
    try:
        api_request = RequestCreateOrganizationDirectory(org_id)
        response = api_request.do_process()

        response = make_response(response, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        # Handle any errors that occur while running the commands
        current_app.logger.error("DirectoryTreeAPI -- create_organization_directory() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::create_organization_directory:: " + str(e), 404
    
    
@directory_tree_api.route('/api/directory/user/<user_id>', methods=['POST', 'OPTIONS'])
def create_user_directory(user_id):
    try:
        api_request = RequestCreateUserDirectory(user_id)
        response = api_request.do_process()

        response = make_response(response, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        # Handle any errors that occur while running the commands
        current_app.logger.error("DirectoryTreeAPI -- create_user_directory() -- Error: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::create_user_directory:: " + str(e), 404