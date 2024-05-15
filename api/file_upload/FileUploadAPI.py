import os
from time import sleep
from flask import Blueprint, current_app, jsonify, make_response, request, flash, url_for
import json
from flask_cors import CORS, cross_origin
from werkzeug.utils import secure_filename
from api.file_upload.handler.RequestGetProjectFiles import RequestGetProjectFiles

from api.file_upload.handler.RequestGroundTruthConversion import RequestGroundTruthConversions
from api.file_upload.handler.RequestUploadFiles import RequestUploadFiles
from api.label_studio.file_import.handler.RequestImportTasks import RequestImportTasks
from api.label_studio.storage.local.entity.PayloadCreateImportStorage import PayloadCreateImportStorage
from api.label_studio.storage.local.handler.RequestCreateImportStorage import RequestCreateImportStorage
from api.label_studio.storage.local.handler.RequestSyncImportStorage import RequestSyncImportStorage
from api.subprocess.handler.HandleUploadGroundTruthLabelStudio import HandleUploadGroundTruthLabelStudio
from dao.TableLsImportStorage import TableLsImportStorage


file_upload_api = Blueprint('file_upload_api', __name__)
CORS(file_upload_api)

@file_upload_api.route('/api/file_upload/ground_truth', methods=['GET'])
def upload_gt():
    # if request.method == 'OPTIONS':
    #     response = make_response('success', 200)
    #     response.headers['Access-Control-Allow-Headers'] = '*'
    #     response.headers['Access-Control-Allow-Origin'] = '*'
    #     response.headers['Content-Type'] = '*'
    #     return response
    
    try:
        # data = json.loads(request.data)
        path = request.args.get('path')

        api_request = RequestGroundTruthConversions(path)
        response = api_request.do_process()

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response
    except Exception as e:
        current_app.logger.error("FileUploadAPI -- upload_gt() -- Error: {}".format(str(e)))
        return "FILE_UPLOAD_API::upload_ground_truth::Error===========>>> " + str(e), 404




@file_upload_api.route('/files/<file_set_id>', methods=['POST', 'OPTIONS'])
def upload_files(file_set_id):

    try:
        file_set_id = int(file_set_id)
        files = request.files.getlist('file')
        data = request.form
        repo_id = data['repo_id']

        dao_import_storage = TableLsImportStorage()
        import_storage = dao_import_storage.read_ls_import_storage_by_repo_id(repo_id)

        current_app.logger.info("FileUploadAPI -- upload_files() -- import_storage: {}".format(import_storage))


        current_app.logger.info("FileUploadAPI -- upload_files() -- data: {}".format(data))

        api_request = RequestUploadFiles(import_storage['project_id'],files, repo_id, file_set_id)
        
        upload_files_response = api_request.do()
        current_app.logger.info("FileUploadAPI -- upload_files() -- upload_files_response: {}".format(upload_files_response))
        
        sleep(1)
    

        payload = {
                    "project": int(import_storage['project_id']),
                    "title": data['title'],
                    "description": data['description'],
                    "path": import_storage['path'],
                    "use_blob_urls": True,
                }

        

        payload = { 
                "project": import_storage['project_id'],
                "use_blob_urls": True
            }
        current_app.logger.info("FileUploadAPI -- upload_files() -- request-sync-import-payload: {}".format(payload))
        api_request = RequestSyncImportStorage(import_storage['ls_id'], payload)
        response = api_request.do()
        current_app.logger.info("FileUploadAPI -- upload_files() -- request-sync-import-response: {}".format(response))

            
        import_xlsx = HandleUploadGroundTruthLabelStudio()
        import_xlsx_response = import_xlsx.do_process(import_storage['project_id'], repo_id)
        current_app.logger.info("FileUploadAPI -- upload_files() -- import_xlsx_response: {}".format(import_xlsx_response))

    
        response = make_response("DONE", 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        current_app.logger.error("FileUploadAPI -- upload_files() -- Error: {}".format(str(e)))
        return "FILE_UPLOAD_API::upload_files::Error===========>>> " + str(e), 404


@file_upload_api.route('/files/<project_id>', methods=['GET'])
def get_project_files(project_id):
    try:

        api_request = RequestGetProjectFiles(project_id)
        response = api_request.do()
        
        

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response, 200
     
    except Exception as e:
        return "Error: " + str(e), 404
