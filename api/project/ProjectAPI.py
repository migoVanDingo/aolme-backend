from api.project.handler.RequestCreateProject import RequestCreateProject
from flask import Blueprint, request
import json
from api.project.handler.RequestDeleteProject import RequestDeleteProject
from api.project.handler.RequestGetProjectById import RequestGetProjectById

from api.project.handler.RequestListAllProjects import RequestListAllProjects
from api.project.handler.RequestListProjectTasks import RequestListProjectTasks
from api.project.handler.RequestUpdateProject import RequestUpdateProject
from api.project.handler.RequestValidateLabelConfig import RequestValidateLabelConfig

project_api = Blueprint('project_api', __name__)

#create project
@project_api.route("/projects", methods=['POST'])
def create_project():
    data = json.loads(request.data)
    api_request = RequestCreateProject(data["name"])
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
    name = data["name"]
    api_request = RequestUpdateProject(project_id, name)
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
@project_api.route("/projects/<project_id>/validate", methods=['POST'])
def validate_label_config(project_id):
    data = json.loads(request.data)
    config = data["config"]
    api_request = RequestValidateLabelConfig(project_id, config)
    response = api_request.do()
    return response
