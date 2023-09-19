import json
from flask import Flask, jsonify, make_response, request
from flask_mysqldb import MySQL
from flask_cors import CORS, cross_origin
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

db = MySQL()
app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'aolme'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'aolmedb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor' 

db.init_app(app)


#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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

