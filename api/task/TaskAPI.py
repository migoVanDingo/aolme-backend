from flask import Blueprint, request
import json

from api.task.handler.RequestCreateTask import RequestCreateTask
from api.task.handler.RequestDeleteTask import RequestDeleteTask
from api.task.handler.RequestGetTaskById import RequestGetTaskById
from api.task.handler.RequestGetTasksList import RequestGetTasksList
from api.task.handler.RequestUpdateTask import RequestUpdateTask



task_api = Blueprint('task_api', __name__)

#create task
@task_api.route("/projects/<project_id>/tasks", methods=['POST'])
def create_task(project_id):
    data = json.loads(request.data)
    api_request = RequestCreateTask(project_id, data["name"])
    response = api_request.do()
    return response


#get tasks list
@task_api.route("/projects/<project_id>/tasks", methods=['GET'])
def get_tasks_list(project_id):
    api_request = RequestGetTasksList(project_id)
    response = api_request.do()
    return response


#get task by id
@task_api.route('/projects/<project_id>/tasks/<task_id>', methods=['GET'])
def get_task(project_id, task_id):
    api_request = RequestGetTaskById(project_id, task_id)
    response = api_request.do()
    return response


#update task
@task_api.route('/projects/<project_id>/tasks/<task_id>', methods=['PATCH'])
def update_task(project_id, task_id):
    data = json.loads(request.data)
    name = data["name"]
    api_request = RequestUpdateTask(project_id, task_id, name)
    response = api_request.do()
    return response


#delete task
@task_api.route("/projects/<project_id>/tasks/<task_id>", methods=['DELETE'])
def delete_task(project_id, task_id):
    api_request = RequestDeleteTask(project_id, task_id)
    response = api_request.do()
    return response