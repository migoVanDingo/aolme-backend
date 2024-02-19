import json
from flask import Blueprint, make_response, request
from flask_cors import CORS

from api.label_studio.ls_project.handler.RequestCreateLsProject import RequestCreateLsProject


label_studio_api = Blueprint('label_studio_api', __name__)
CORS(label_studio_api)

@label_studio_api.route('/api/label_studio/project', methods=['POST', 'OPTIONS'])
def create_project():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    data = json.loads(request.data)
    print("args: {}".format(data))
    api_request = RequestCreateLsProject()

    response = api_request.do_process(data)
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
