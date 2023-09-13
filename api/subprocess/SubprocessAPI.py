import subprocess, json
from flask_cors import CORS
from flask import Blueprint, make_response, request


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
    
    data = json.loads(request.data)
    commands = [
        "cd /Users/bubz/Developer/master-project/label-studio",   # Replace with your first command and its arguments
        ". ~/.bash_profile",
        "label-studio",   # Replace with your second command and its arguments

    ]


    try:
    # Run each command sequentially
        for command in commands:
            subprocess.run(command, shell=True, check=True)

        print("All commands executed successfully.")

        response = make_response("success", 204)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur while running the commands
        print("Error:", e)
        return e
