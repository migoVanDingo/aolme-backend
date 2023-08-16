from api.project.handler.RequestCreateProject import RequestCreateProject
from flask import Blueprint, request
import json
from api.project.handler.RequestDeleteProject import RequestDeleteProject
from api.project.handler.RequestGetProjectById import RequestGetProjectById

from api.project.handler.RequestListAllProjects import RequestListAllProjects
from api.project.handler.RequestListProjectTasks import RequestListProjectTasks
from api.project.handler.RequestUpdateProject import RequestUpdateProject
from api.project.handler.RequestValidateLabelConfig import RequestValidateLabelConfig
from api.project.utility.ProjectPayloads import ProjectPayloads
from api.project.utility.validator.ProjectValidator import ProjectValidator

project_api = Blueprint('project_api', __name__)

#create project
@project_api.route("/projects", methods=['POST'])
def create_project():

    data = json.loads(request.data)

    #validate request data
    validator = ProjectValidator()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        return is_valid[1]
    
    #make POST request to label-studio
    api_request = RequestCreateProject(data)
    response = api_request.do()


    return response


#get project list
@project_api.route("/projects", methods=['GET'])
def get_projects_list():
    api_request = RequestListAllProjects()
    response = api_request.do()
    return response


#get project by id
@project_api.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    api_request = RequestGetProjectById(project_id)
    response = api_request.do()
    return response


#update project
@project_api.route('/projects/<project_id>', methods=['PATCH'])
def update_project(project_id):
    data = json.loads(request.data)
    
    validator = ProjectValidator()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        return is_valid[1]


    api_request = RequestUpdateProject(project_id, data)
    response = api_request.do()
    return response


#delete project
@project_api.route("/projects/<project_id>", methods=['DELETE'])
def delete_project(project_id):
    api_request = RequestDeleteProject(project_id)
    response = api_request.do()
    return response


#List all tasks for a project
@project_api.route("/projects/<project_id>/tasks", methods=['GET'])
def list_project_tasks(project_id):
    api_request = RequestListProjectTasks(project_id)
    response = api_request.do()
    return response


#Validate Label config
@project_api.route("/projects/validate", methods=['POST'])
def validate_label_config():
    data = json.loads(request.data)
    
    api_request = RequestValidateLabelConfig(data)
    response = api_request.do()
    return response
