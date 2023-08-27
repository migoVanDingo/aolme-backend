from flask import Blueprint, request
import json
from api.label_studio.task.Entity.PayloadGetTaskList import PayloadGetTaskList

from api.label_studio.task.handler.RequestCreateTask import RequestCreateTask
from api.label_studio.task.handler.RequestDeleteTask import RequestDeleteTask
from api.label_studio.task.handler.RequestGetTaskById import RequestGetTaskById
from api.label_studio.task.handler.RequestGetTasksList import RequestGetTasksList
from api.label_studio.task.handler.RequestUpdateTask import RequestUpdateTask
from api.label_studio.task.Entity.PayloadCreateTask import PayloadCreateTask



task_api = Blueprint('task_api', __name__)

#create task
@task_api.route("/projects/tasks", methods=['POST'])
def create_task():
    data = json.loads(request.data)

    validator = PayloadCreateTask()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        return is_valid[1]

    api_request = RequestCreateTask(data)
    response = api_request.do()
    return response


#get tasks list
@task_api.route("/projects/tasks", methods=['GET'])
def get_tasks_list():
    data = json.loads(request.data)

    validator = PayloadGetTaskList()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        return is_valid[1]

    api_request = RequestGetTasksList(data)
    response = api_request.do()
    return response


#get task by id
@task_api.route('/projects/tasks/<task_id>', methods=['GET'])
def get_task(task_id):
    api_request = RequestGetTaskById(task_id)
    response = api_request.do()
    return response


#update task
@task_api.route('/projects/<project_id>/tasks/<task_id>', methods=['PATCH'])
def update_task(project_id, task_id):
    data = json.loads(request.data)


    validator = PayloadCreateTask()
    is_valid = validator.validate(data)
    if is_valid[0] is False:
        return is_valid[1]
    

    api_request = RequestUpdateTask(project_id, task_id, data)
    response = api_request.do()
    return response


#delete task
@task_api.route("/projects/tasks/<task_id>", methods=['DELETE'])
def delete_task(task_id):
    api_request = RequestDeleteTask(task_id)
    response = api_request.do()
    return response