import json
from flask import Blueprint, make_response, request
from flask_cors import CORS
from api.label_studio.ls_project.handler.RequestGetLsProjectByRepoId import RequestGetLsProjectByRepoId

from api.label_studio.ls_project.handler.RequestCreateLsProject import RequestCreateLsProject



label_studio_api = Blueprint('label_studio_api', __name__)
CORS(label_studio_api)

@label_studio_api.route('/api/label_studio/repo/<repo_id>', methods=['GET'])
def get_repo_project_by_id(repo_id):
    print("get_repo_project_by_id: {}".format(repo_id))
    api_request = RequestGetLsProjectByRepoId(repo_id)
    response = api_request.do_process()

    print("responseRRR: {}".format(response))

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    
    return response

@label_studio_api.route('/api/label_studio/project', methods=['POST', 'OPTIONS'])
def create_project():

    data = json.loads(request.data)
    print("args: {}".format(data))
    api_request = RequestCreateLsProject()

    response = api_request.do_process(data)
    

    response = make_response(response, 200)
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = '*'
    return response
