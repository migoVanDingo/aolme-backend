import os, json
import subprocess
from dotenv import load_dotenv
from flask import jsonify, request
import requests
load_dotenv()
class HandleUploadGroundTruthLabelStudio:
    def __init__(self):
        self.url = "http://localhost:8080/api/projects/"
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']

    def do_process(self, project_id, entity_id, dataset_id, subset_id):
        try:
            path = "/Users/bubz/Developer/master-project/aolme-backend/_fs/organization/"+entity_id+"/dataset/"+dataset_id+"/subset/"+subset_id+"/ground-truth-raw"
            files = os.listdir(path)
            arr = []
            for f in files:
                f = "{}/{}".format(path, f)
                print("HandleUploadGroundTruthLabelStudio -- files: {}".format(f))
                arr.append(f)


            for file_name in arr:
                print("fn: {}".format(file_name))
                url = f"{self.url}{project_id}/import"
                headers = {
                'Authorization': f'Token {self.token}',
                }
                post_files = {
                    'file': (file_name, open(file_name, 'rb')),
                }

                try:
                    response = requests.post(url, headers=headers, files=post_files)
                    if response.status_code == 201:
                        print(f"Successfully imported {file_name} to project {project_id}")
                    # You can process the response content here if needed
                    else:
                        print(f"Failed to import {file_name} to project {project_id}. Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error while importing {file_name} to project {project_id}: {str(e)}")

            print("All commands executed successfully.")
            return "success"
        except subprocess.CalledProcessError as e:
            return "Error yo: " + str(e), 404
        

    def execute_curl_for_file_names(file_names, project_id, project_token=os.environ['LABEL_STUDIO_SECRET_KEY'], api_ur='http://localhost:8080'):
            print("FILE_NAMES: {}".format(file_names))
            for file_name in file_names:
                print("fn: {}".format(file_name))
                url = f"{self.url}/api/projects/{project_id}/import"
                headers = {
                'Authorization': f'Token {project_token}',
                }
                files = {
                    'file': (file_name, open(file_name, 'rb')),
                }

                try:
                    response = requests.post(url, headers=headers, files=files)
                    if response.status_code == 200:
                        print(f"Successfully imported {file_name} to project {project_id}")
                    # You can process the response content here if needed
                    else:
                        print(f"Failed to import {file_name} to project {project_id}. Status code: {response.status_code}")
                except Exception as e:
                    print(f"Error while importing {file_name} to project {project_id}: {str(e)}")
