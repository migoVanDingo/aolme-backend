import subprocess, json, os
from flask_cors import CORS
from flask import Blueprint, make_response, request
from dotenv import load_dotenv
from api.subprocess.handler.HandleLSExportAllFrames import HandleLSExportAllFrames
from dao.TableSubset import TableSubset
from file_watcher.WatchNotebook import WatchNotebook

from utility.Directory import Directory
load_dotenv()

from api.subprocess.handler.HandleUploadGroundTruthLabelStudio import HandleUploadGroundTruthLabelStudio


subprocess_api = Blueprint("subprocess_api", __name__)
CORS(subprocess_api)


@subprocess_api.route('/subprocess/label-studio', methods=["POST", "OPTIONS", "GET"])
def start_label_studio_project():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    
    #data = json.loads(request.data)
    commands = [
        "cd /Users/bubz/Developer/master-project/label-studio",
        "label-studio",
    ]

    print('LABEL-STUDIO JSON: {}'.format(commands))

    # "export LABEL_STUDIO_USERNAME=a@a.com",
    #"export LABEL_STUDIO_PASSWORD=Migo1234!",
    env = os.environ.copy()
    print('LABEL-STUDIO ENV: {}'.format(env))
    try:
    # Run each command sequentially
        for command in commands:
            subprocess.run(command, shell=True, check=True, env=env)

        print("All commands executed successfully.")

        response = make_response("success", 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the commands
        print("Error:", e)
        return "Error: " + str(e), 404


@subprocess_api.route('/file/upload', methods=['POST', 'OPTIONS'])
def upload_files_to_project():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    
    data = json.loads(request.data)

    
    try:
        import_xlsx = HandleUploadGroundTruthLabelStudio()
        import_xlsx_response = import_xlsx.do_process(data['project_id'])

        response = make_response(import_xlsx_response, 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the commands
        print("Error:", e)
        return "Error: " + str(e), 404
    


@subprocess_api.route('/subprocess/jupyter', methods=['POST', 'OPTIONS'])
def start_jupyter_notebook():
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    
    data = json.loads(request.data)


    # create_dir = Directory.create_directory(data['project_id'], data['folder_name'])

    # print("create_dir: {}".format(create_dir['path']))
    
    # if data['entity_id'].startswith("ORG"):
    #     dir = os.environ['ORGANIZATION_DIRECTORY']
    # elif data['entity_id'].startswith("USR"):
    #     dir = os.environ['USER_DIRECTORY']

    # path = os.path.join(dir, data['entity_id'])
    # path = os.path.join(path, 'notebook')

    path = os.path.join(os.environ['REPO_DIRECTORY'], data['repo_id'])
    path = os.path.join(path, 'notebook')

    
    commands = [
        "jupyter lab"
    ]

    print("Commands: {}".format(commands))

    try:
        os.chdir(path)
        # Run each command sequentially
        for command in commands:
            subprocess.run(command, shell=True, check=True)

        payload_insert_file = {
            "entity_id": data["repoEntity"],
            "description": "JUPYTER NOTEBOOK",
            "owner": data['owner'],
            "type": "NOTEBOOK",
            "is_public": data['is_public'],
            "repo_id": data["repoId"],
            "is_active": 1, 

        }

        #watcher = WatchNotebook()
        #watcher.fileWatcher(path, 1, payload_insert_file)

        print("All commands executed successfully.")

        response = make_response("SUCCESS", 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the commands
        print("Error:", e)
        return "Error: " + str(e), 404


@subprocess_api.route('/subprocess/label-studio/export-all-frames', methods=['GET'])
def export_all_frames():
    try:
        dataset_id = request.args.get('dataset_id')
        subset_id = request.args.get('subset_id')
        entity_id = request.args.get('entity_id')
        project_id = request.args.get('project_id')

        request = HandleLSExportAllFrames(entity_id, dataset_id, subset_id, project_id)

        response = make_response("success", 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except Exception as e:
        print("SubprocessAPI::export_all_frames::Error: {}".format(str(e)))
        return "SubprocessAPI::export_all_frames::Error: {}".format(str(e)), 404



