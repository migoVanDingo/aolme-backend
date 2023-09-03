from flask import Blueprint, request
import json
from api.label_studio.file_import.handler.RequestDeleteFileUpload import RequestDeleteFileUpload
from api.label_studio.file_import.handler.RequestDeleteFiles import RequestDeleteFiles

from api.label_studio.file_import.handler.RequestGetFileUpload import RequestGetFileUpload
from api.label_studio.file_import.handler.RequestGetFilesList import RequestGetFilesList
from api.label_studio.file_import.handler.RequestImportTasks import RequestImportTasks
from api.label_studio.file_import.handler.RequestUpdateFileUpload import RequestUpdateFileUpload

import_api = Blueprint('import_api', __name__)

@import_api.route('/import/file-upload/<file_id>', methods=['GET'])
def get_file_upload(file_id):
    api_request = RequestGetFileUpload()
    response = api_request.do()
    return response


@import_api.route('/projects/<project_id>/file-uploads', methods=['GET'])
def get_files_list(project_id):
    api_request = RequestGetFilesList()
    response = api_request.do()
    return response


@import_api.route('/import/file-upload/<file_id>', methods=['PATCH'])
def update_file_upload(file_id):
    api_request = RequestUpdateFileUpload()
    response = api_request.do()
    return response


@import_api.route('/import/file-upload/<file_id>', methods=['DELETE'])
def delete_file_upload(file_id):
    api_request = RequestDeleteFileUpload()
    response = api_request.do()
    return response


@import_api.route('/projects/<project_id>/file-uploads', methods=['DELETE'])
def delete_files(file_id):
    api_request = RequestDeleteFiles()
    response = api_request.do()
    return response


@import_api.route('/projects/<project_id>/import', methods=['POST'])
def import_tasks(project_id):
    api_request = RequestImportTasks(project_id)
    response = api_request.do()
    return response