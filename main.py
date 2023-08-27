import json
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS, cross_origin
from api.label_studio.task.TaskAPI import task_api
from api.label_studio.project.ProjectAPI import project_api
from api.label_studio.file_export.ExportAPI import file_export_api
from api.label_studio.file_import.ImportAPI import import_api
from api.label_studio.storage.local.LocalStorageAPI import local_storage_api
from api.file_upload.FileUploadAPI import file_upload_api


app = Flask(__name__)
CORS(app)


#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(task_api)
app.register_blueprint(project_api)
app.register_blueprint(file_export_api)
app.register_blueprint(import_api)
app.register_blueprint(local_storage_api)
app.register_blueprint(file_upload_api)

@app.route("/", methods=["GET", "OPTIONS"])
def hello_world():
    return "Hello World"


@app.route('/', methods=['POST', 'OPTIONS'])
def test():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'

        return response
    
    data = request.json
    data = {
        "data":data,
        "newField":"yuh-momma"
    }
    response = make_response(data, 200)
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
