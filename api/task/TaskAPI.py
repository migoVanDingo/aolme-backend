from flask import Blueprint

task_api = Blueprint('task_api', __name__)

#create task
@task_api.route("/", methods=['POST'])
def create_task():
    return "create task"

#get tasks list
@task_api.route("/", methods=['GET'])
def get_tasks_list():
    return "task lists"

#get task by id
@task_api.route('/<task_id>', methods=['GET'])
def get_task(task_id):
    return 'get by id {}'.format(task_id)

#update task
@task_api.route('/<task_id>', methods=['PATCH'])
def update_task(task_id):
    return "update {}".format(task_id) 

#delete task
@task_api.route("/<task_id>", methods=['DELETE'])
def delete_task(task_id):
    return "delete lists {}".format(task_id)