import os
from flask import Blueprint, jsonify, make_response, request, flash, url_for
import json
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from api.project.handler.RequestCreateRepoProject import RequestCreateRepoProject
from api.project.handler.RequestGetProjectById import RequestGetProjectById
from api.project.handler.RequestGetProjectList import RequestGetProjectList

from api.project.utility.validator.CreateProjectValidator import CreateProjectValidator
project_repo_api = Blueprint('project_repo_api', __name__)
CORS(project_repo_api)

@project_repo_api.route('/repo/project/create', methods=['POST', 'OPTIONS'])
def create_project_in_repo():
    try:
        if request.method == 'OPTIONS':
            response = make_response('success', 200)
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Content-Type'] = '*'
            return response

        
        if request.method == 'POST':
            data = json.loads(request.data)
            validator = CreateProjectValidator()
            is_valid = validator.validate(data)
            if is_valid[0] is False:
                return is_valid[1]

        
            api_request = RequestCreateRepoProject(data)
        
            return api_request.do(), 200
        
        
    except Exception as e:
        return "Error: " + str(e), 404
    
@project_repo_api.route('/repo/project/<project_id>', methods=['GET'])
def get_repo_project_by_id(project_id):
    try:

        api_request = RequestGetProjectById(project_id)
        
        return api_request.do(), 200
        
        
    except Exception as e:
        return "Error: " + str(e), 404
    


@project_repo_api.route('/repo/project/list', methods=['GET'])
def get_repo_project_list():
    try:

        api_request = RequestGetProjectList()
        
        return api_request.do(), 200
        
        
    except Exception as e:
        return "Error: " + str(e), 404