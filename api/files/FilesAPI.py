import json
from flask import Blueprint, make_response, request
from flask_cors import CORS

from api.files.handler.RequestCreateFileRecord import RequestCreateFileRecord
from api.files.handler.RequestUploadFile import RequestUploadFile


files_api = Blueprint('files_api', __name__)
CORS(files_api)

@files_api.route('/api/files', methods=['POST', 'OPTIONS'])
def create_file():
    try:
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
        api_request = RequestCreateFileRecord(data, files, repo_id)
        response = api_request.do_process()
        

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
        
    except Exception as e:
        print("FilesAPI::create_file()::Error: " + str(e))
        return "FilesAPI::create_file()::Error: " + str(e), 404