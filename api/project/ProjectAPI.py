from api.project.handler.RequestCreateProject import RequestCreateProject
from flask import Blueprint, request
import json
from api.project.handler.RequestDeleteProject import RequestDeleteProject
from api.project.handler.RequestGetProjectById import RequestGetProjectById

from api.project.handler.RequestListAllProjects import RequestListAllProjects
from api.project.handler.RequestUpdateProject import RequestUpdateProject

project_api = Blueprint('project_api', __name__)

#create task
@project_api.route("/projects", methods=['POST'])
def create_project():
    data = json.loads(request.data)
    api_request = RequestCreateProject()
    response = api_request.do()
    return response


#get project list
@project_api.route("/projects", methods=['GET'])
def get_tasks_list():
    api_request = RequestListAllProjects()
    response = api_request.do()
    return response


#get project by id
@project_api.route('/projects/<project_id>', methods=['GET'])
def get_task(project_id):
    api_request = RequestGetProjectById(project_id)
    response = api_request.do()
    return response


#update project
@project_api.route('/projects/<project_id>', methods=['PATCH'])
def update_task(project_id):
    data = json.loads(request.data)
    name = data["name"]
    api_request = RequestUpdateProject(project_id, name)
    response = api_request.do()
    return response


#delete task
@project_api.route("/projects/<project_id>", methods=['DELETE'])
def delete_task(project_id, task_id):
    api_request = RequestDeleteProject(project_id)
    response = api_request.do()
    return response