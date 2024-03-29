import os
from time import sleep
from flask import Blueprint, jsonify, make_response, request, flash, url_for
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
        print("FILE_UPLOAD_API::upload_ground_truth::Error===========>>> " + str(e))
        return "FILE_UPLOAD_API::upload_ground_truth::Error===========>>> " + str(e), 404




@file_upload_api.route('/files/<project_id>/<file_set_id>', methods=['POST', 'OPTIONS'])
def upload_files(project_id, file_set_id):
    if request.method == 'OPTIONS':
        response = make_response('success', 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'

        return response
    

    try:
        files = request.files.getlist('file')
        data = request.form
        repo_id = data['repo_id']
        print("Files length: {}".format(len(files)))
        print('FileUploadAPI project_id: {} --- {}'.format(project_id, project_id))
        print("REPO ID: {}".format(repo_id))    
        api_request = RequestUploadFiles(project_id,files, repo_id, file_set_id)
        
        upload_files_response = api_request.do()
        print("FileUploadAPI -- RequestUploadFiles response: {}".format(upload_files_response))
        
        sleep(1)
    

        payload = {
                    "project": int(project_id),
                    "title": data['title'],
                    "description": data['description'],
                    "path": data['path'],
                    "use_blob_urls": True,
                }

        print("TRIPPING payload: {}".format(payload))
        validator = PayloadCreateImportStorage()
        is_valid = validator.validate(payload)
        if is_valid[0] is False:
            print("TRIPPING is_valid: {}".format(is_valid[1]))
            return is_valid[1]
        
        print("PRE -- RequestCreateImportStorage")
        api_request = RequestCreateImportStorage(payload)
        local_storage_response = api_request.do()


        print("FileUploadAPI -- RequestCreateImportStorage response: {}".format(local_storage_response))
        #print("localStorage response: {}".format(local_storage))
            

        payload = { 
                "project": project_id,
                "use_blob_urls": True
            }

        api_request = RequestSyncImportStorage(local_storage_response['id'], payload)
        response = api_request.do()
        print("FileUploadAPI -- RequestSyncImportStorage response: {}".format(response))
        #print("sync storage {}".format(sync_storage_response))

            
        import_xlsx = HandleUploadGroundTruthLabelStudio()
        import_xlsx_response = import_xlsx.do_process(project_id, repo_id)
        print("Upload gt response: {}".format(import_xlsx_response))

    
        response = make_response("DONE", 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response

    except Exception as e:
        print("Error yoseph: {}".format(str(e)))
        return "Error yosephat: " + str(e), 404


@file_upload_api.route('/files/<project_id>', methods=['GET'])
def get_project_files(project_id):
    try:

        api_request = RequestGetProjectFiles(project_id)
        response = api_request.do()
        #print('response: {}'.format(response))
        
        

        response = make_response(response, 200)
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Content-Type'] = '*'
        return response, 200
     
    except Exception as e:
        return "Error: " + str(e), 404


# UPLOAD_FOLDER = '/uploads'
# ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'json', 'csv'}

# @file_upload_api.route("/upload", methods=['POST', 'OPTIONS'])
# def upload_files():
    
    
#     if request.method == 'OPTIONS':
#         response = make_response('success', 200)
#         response.headers['Access-Control-Allow-Headers'] = '*'
#         response.headers['Access-Control-Allow-Origin'] = '*'
#         response.headers['Content-Type'] = '*'

#         return response

#     """ if 'file' not in request.files:
#         response = make_response('No file found', 500)
#         return response """
    
#     files = request.files.getlist('file')
#     print(len(files))


#         # If the user does not select a file, the browser submits an
#         # empty file without a filename.

#     for file in files:

#         if file.filename == '':
#             response = make_response('File must have name', 500)
#             return response
    
#         # Create the uploads directory
#         current_directory = os.getcwd()
#         uploads_directory = os.path.join(current_directory, 'uploads')
    
#         if file and allowed_file(file.filename):
#             #filename = secure_filename(file.filename)
#             print(os.path.join(uploads_directory, file.filename))
#             file.save(os.path.join(uploads_directory, file.filename))
#             #print(jsonify(url_for('download_file', name=file.filename)))
            
#         print(file.filename)

#     response = make_response('success', 200)
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     return response
    
# def allowed_file(filename):
#     return '.' in filename and \
#            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

