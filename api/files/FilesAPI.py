import json
from flask import Blueprint, make_response, request
from flask_cors import CORS

from api.files.handler.RequestUploadFile import RequestUploadFile


files_api = Blueprint('files_api', __name__)
CORS(files_api)

@files_api.route('/files/<project_id>', methods=['POST', 'OPTIONS'])
def create_file():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    
    try:
       
        files = request.files.getlist('file')
        data = request.form
        api_request = RequestUploadFile(json.loads(request.data))
        response = api_request.do_process()

    
        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    
    
    except Exception as e:
        print(str(e))
        return "Error: " + str(e), 404