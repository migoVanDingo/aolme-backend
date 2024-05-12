import os, json
import subprocess
from dotenv import load_dotenv
from flask import current_app, jsonify, request
import requests
load_dotenv()
class HandleUploadGroundTruthLabelStudio:
    def __init__(self):
        self.url = "http://localhost:8080/api/projects/"
        self.token= os.environ['LABEL_STUDIO_SECRET_KEY']

    def do_process(self, project_id, entity_id, dataset_id, subset_id):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: entity_id: {entity_id} :: dataset_id: {dataset_id} :: subset_id: {subset_id} :: project_id: {project_id}")
            path = "/Users/bubz/Developer/master-project/aolme-backend/_fs/organization/"+entity_id+"/dataset/"+dataset_id+"/subset/"+subset_id+"/ground-truth-raw"
            current_app.logger.info(f"{self.__class__.__name__} :: path: {path}")   

            files = os.listdir(path)
            arr = []
            for f in files:
                f = "{}/{}".format(path, f)
                current_app.logger.info(f"{self.__class__.__name__} :: files: {f}")
                arr.append(f)


            for file_name in arr:
                current_app.logger.info(f"{self.__class__.__name__} :: file_name: {file_name}")
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
                        current_app.logger.info(f"{self.__class__.__name__} :: Successfully imported {file_name} to project {project_id}")
                    # You can process the response content here if needed
                    else:
                        current_app.logger.error(f"{self.__class__.__name__} :: Failed to import {file_name} to project {project_id}. Status code: {response.status_code}")
                except Exception as e:
                    current_app.logger.error(f"{self.__class__.__name__} :: Error while importing {file_name} to project {project_id}: {str(e)}")

            current_app.logger.info(f"{self.__class__.__name__} :: Successfully imported all files to project {project_id}")
            return "success"
        except subprocess.CalledProcessError as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} " + str(e), 404
        

    def execute_curl_for_file_names(self, file_names, project_id, project_token=os.environ['LABEL_STUDIO_SECRET_KEY'], api_ur='http://localhost:8080'):
            current_app.logger.info(f"{self.__class__.__name__} :: file_names: {file_names} :: project_id: {project_id}")
            for file_name in file_names:
                current_app.logger.info(f"{self.__class__.__name__} :: file_name: {file_name}")
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
                        current_app.logger.info(f"{self.__class__.__name__} :: Successfully imported {file_name} to project {project_id}")
                    # You can process the response content here if needed
                    else:
                        current_app.logger.error(f"{self.__class__.__name__} :: Failed to import {file_name} to project {project_id}. Status code: {response.status_code}")
                      
                except Exception as e:
                    current_app.logger.error(f"{self.__class__.__name__} :: Error while importing {file_name} to project {project_id}: {str(e)}")
                
