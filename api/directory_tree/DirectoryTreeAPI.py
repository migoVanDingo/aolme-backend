from datetime import datetime
import json
from flask import Blueprint, jsonify, make_response, request
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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::get_project_root:: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_project_root:: " + str(e), 404
   

@directory_tree_api.route('/api/directory/entity/<entity_id>/folder/<folder_name>/owner/<owner_id>/repo/<repo_id>', methods=['GET'])
def get_directory_items(entity_id, folder_name, owner_id, repo_id):
    try:
 
        print("API Request received: {}".format(datetime.now()))
        api_request = RequestGetFolderItems(entity_id, folder_name, owner_id, repo_id)
        response = api_request.do_process()

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
       
    except Exception as e:
        print("CLASS::DirectoryTreeAPI::ENDPOINT::get_directory_items:: {}".format(str(e)))
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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::get_folder_items:: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_folder_items:: " + str(e), 404






     
""" @directory_tree_api.route('/api/directory/project/<project_id>/folder', methods=['GET'])
def get_folder_items(project_id):
    try:
        if request.args.get('fa') is None:
            return "DirectoryTreeAPI -- get_project_root() -- Error: Bad request - No request Args " + str(e), 417
        
       
        rawrgs = request.args.get('fa')
        
        args = rawrgs.split(',')

        if args is not None:
            print('args: {}'.format(args))
            directory_read_request = ReadProjectFolder(project_id, args)
            dir_read_response = directory_read_request.do()
        else:
            print('somehting is wrong0')

        
        print('dir_read_response: {}'.format(dir_read_response))
        response = make_response(dir_read_response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response """
       
""" except Exception as e:
        print("CLASS::DirectoryTreeAPI::ENDPOINT::get_folder_items:: {}".format(str(e)))
        return "CLASS::DirectoryTreeAPI::ENDPOINT::get_folder_items:: " + str(e), 404 """
    

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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::create_directory:::", e)
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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::create_project_directory:::", e)
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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::create_organization_directory:::", e)
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
        print("CLASS::DirectoryTreeAPI::ENDPOINT::create_user_directory:::", e)
        return "CLASS::DirectoryTreeAPI::ENDPOINT::create_user_directory:: " + str(e), 404