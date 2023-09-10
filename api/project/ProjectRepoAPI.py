import os
from flask import Blueprint, jsonify, make_response, request, flash, url_for
import json
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from api.file_upload.handler.RequestUploadFiles import RequestUploadFiles
from api.label_studio.project.handler.RequestCreateProject import RequestCreateProject
from api.label_studio.storage.local.entity.PayloadCreateImportStorage import PayloadCreateImportStorage
from api.label_studio.storage.local.handler.RequestCreateImportStorage import RequestCreateImportStorage
from api.label_studio.storage.local.handler.RequestSyncImportStorage import RequestSyncImportStorage
from api.label_studio.webhook.handler.RequestCreateWebhook import RequestCreateWebhook
from api.project.handler.RequestCreateRepoProject import RequestCreateRepoProject
from api.project.handler.RequestGetProjectById import RequestGetProjectById
from api.project.handler.RequestGetProjectList import RequestGetProjectList

from api.project.utility.validator.CreateProjectValidator import CreateProjectValidator
from api.webhook_handler.handler.HandleProjectUpdate import HandleProjectUpdate
project_repo_api = Blueprint('project_repo_api', __name__)
CORS(project_repo_api)

@project_repo_api.route('/repo/project/create', methods=['POST', 'OPTIONS'])
def create_project_in_repo():
    try:
        if request.method == 'OPTIONS':
            response = make_response('success', 200)
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Content-Type'] = '*'
            return response

        
        if request.method == 'POST':
            data = json.loads(request.data)
            validator = CreateProjectValidator()
            is_valid = validator.validate(data)
            if is_valid[0] is False:
                return is_valid[1]
            
            payload = {
                "title": data['name'],
                "description": data['description']
            }
            api_request = RequestCreateProject(payload)
            label_studio_project = api_request.do()
            print("lsPRO: {}".format(label_studio_project))

            payload_create_webhook = {
                "actions": [
                "PROJECT_UPDATED"
                ],
                "headers": {},
                "is_active": True,
                "project": label_studio_project['id'],
                "send_for_all_actions": True,
                "send_payload": True,
                "url": "http://127.0.0.1:5000/api/webhook-handler/project-created"
            }

            print('MY payload : {}'.format(payload))

            create_webhook = RequestCreateWebhook(payload_create_webhook)
            response = create_webhook.do()


        
            #Create project in my app
            if label_studio_project is not None:
                #print('ls project ID: {}'.format(label_studio_project['id']))
                payload = {
                    "name": data['name'],
                    "description": data['description'],
                    "owner": data['owner'],
                    "created_by": data['created_by'],
                    "last_updated_by": data['last_updated_by'],
                    "ls_project_id":label_studio_project['id'] 
                }
                api_request = RequestCreateRepoProject(payload)

                repo_project = api_request.do()
                #print("repo project response: {}".format(repo_project.data))

            #Create project in Label Studio
            # if repo_project is not None:
            #     payload = {
            #         "title": data['name'],
            #         "description": data['description']
            #     }
            #     api_request = RequestCreateProject(payload)
            #     label_studio_project = api_request.do()
            #     print(label_studio_project)

            #Add Local storage to Label Studio project
            if label_studio_project is not None:  
                response = {
                    "project_id": label_studio_project['id'],
                    "title": data['name'],
                    "description": data['description'],
                    "path": "/Users/bubz/Developer/master-project/aolme-backend/uploads/{}/videos".format(label_studio_project['id']),
                    "use_blob_urls": True,
                }
                # validator = PayloadCreateImportStorage()
                # is_valid = validator.validate(payload)
                # if is_valid[0] is False:
                #     return is_valid[1]
                # api_request = RequestCreateImportStorage(payload)
                # local_storage = api_request.do()
                # print(local_storage)

                
                """ response = {
                    "project_id":label_studio_project['id'],
                    "local_storage_id": local_storage['id']
                    } """
                   



            
            
            # if label_studio_project is not None:
                
            #     api_request = RequestUploadFiles(files)
            #     upload_files_response = api_request.do()
                
            
            return response, 200
        
        
    except Exception as e:
        print(str(e))
        return "Error: " + str(e), 404
    
@project_repo_api.route('/repo/project/<project_id>', methods=['GET'])
def get_repo_project_by_id(project_id):
    try:

        api_request = RequestGetProjectById(project_id)
        
        res = api_request.do()
        response = make_response(res, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
        
        
    except Exception as e:
        return "Error: " + str(e), 404
    


@project_repo_api.route('/repo/project/list', methods=['GET'])
def get_repo_project_list():
    try:

        api_request = RequestGetProjectList()
        
        return api_request.do(), 200
        
        
    except Exception as e:
        return "Error: " + str(e), 404