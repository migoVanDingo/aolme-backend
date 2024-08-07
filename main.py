import json
from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
import logging
from api.label_studio.task.TaskAPI import task_api
from api.label_studio.project.ProjectAPI import project_api
from api.label_studio.file_export.ExportAPI import file_export_api
from api.label_studio.file_import.ImportAPI import import_api
from api.label_studio.storage.local.LocalStorageAPI import local_storage_api
from api.file_upload.FileUploadAPI import file_upload_api
from api.project.ProjectRepoAPI import project_repo_api
from api.label_studio.webhook.WebhookAPI import webhook_api
from api.webhook_handler.WebhookHandlerAPI import webhook_handler_api
from api.subprocess.SubprocessAPI import subprocess_api
from api.directory_tree.DirectoryTreeAPI import directory_tree_api
from api.user.UserAPI import user_api
from api.organization.OrganizationAPI import organization_api
from api.entity_user.EntityUserApi import entity_user_api
from api.repository.RepositoryAPI import repository_api
from api.config.ConfigAPI import config_api
from api.module.ModuleAPI import module_api
from api.dataset.DatasetAPI import dataset_api
from api.files.FilesAPI import files_api
from api.label_studio.ls_project.LabelStudioAPI import label_studio_api

logging.basicConfig(filename='record.log',
                    level=logging.DEBUG, format='%(asctime)s | %(levelname)s | %(lineno)d | \n %(message)-20s')

db = MySQL()
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aolme_db_v2'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aolme_db_v2'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

db.init_app(app)


# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.before_request
def handle_options():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response


app.register_blueprint(task_api)
app.register_blueprint(project_api)
app.register_blueprint(file_export_api)
app.register_blueprint(import_api)
app.register_blueprint(local_storage_api)
app.register_blueprint(file_upload_api)
app.register_blueprint(project_repo_api)
app.register_blueprint(webhook_api)
app.register_blueprint(webhook_handler_api)
app.register_blueprint(subprocess_api)
app.register_blueprint(directory_tree_api)
app.register_blueprint(user_api)
app.register_blueprint(organization_api)
app.register_blueprint(entity_user_api)
app.register_blueprint(repository_api)
app.register_blueprint(config_api)
app.register_blueprint(module_api)
app.register_blueprint(dataset_api)
app.register_blueprint(files_api)
app.register_blueprint(label_studio_api)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
