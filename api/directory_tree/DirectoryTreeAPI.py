import json
from flask import Blueprint, jsonify, make_response, request
from flask_cors import CORS
from api.directory_tree.handler.ReadProjectFolder import ReadProjectFolder

from api.directory_tree.handler.ReadProjectRoot import ReadProjectRoot
from utility.Directory import Directory


directory_tree_api = Blueprint('directory_tree_api', __name__)
CORS(directory_tree_api)

@directory_tree_api.route('/directory/project/<project_id>/root', methods=['GET'])
def get_project_root(project_id):
   try:
        
        
        directory_read_request = ReadProjectRoot(project_id)
            
        dir_read_res = directory_read_request.do()

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
        print("Error yoseph: {}".format(str(e)))
        return "Error yosephat: " + str(e), 404

     
@directory_tree_api.route('/directory/project/<project_id>/folder', methods=['GET'])
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
        return response
       
    except Exception as e:
        print("Error yoseph: {}".format(str(e)))
        return "Error yosephat: " + str(e), 404
    

@directory_tree_api.route('/directory/project/<project_id>/new', methods=['POST', 'OPTIONS'])
def create_directory(project_id):
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    
    try:

        data = json.loads(request.data)
    
        create_dir = Directory.create_directory(project_id, data['name'])

        response = make_response(create_dir, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        # Handle any errors that occur while running the commands
        print("Error:", e)
        return "Error: " + str(e), 404