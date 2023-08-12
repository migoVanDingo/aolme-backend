from flask import Blueprint, request
import json

from api.storage.local.handler.RequestCreateExportStorage import RequestCreateExportStorage
from api.storage.local.handler.RequestCreateImportStorage import RequestCreateImportStorage
from api.storage.local.handler.RequestDeleteExportStorage import RequestDeleteExportStorage
from api.storage.local.handler.RequestDeleteImportStorage import RequestDeleteImportStorage
from api.storage.local.handler.RequestGetAllExportStorage import RequestGetAllExportStorage
from api.storage.local.handler.RequestGetAllImportStorage import RequestGetAllImportStorage
from api.storage.local.handler.RequestGetExportStorage import RequestGetExportStorage
from api.storage.local.handler.RequestGetImportStorage import RequestGetImportStorage
from api.storage.local.handler.RequestSyncExportStorage import RequestSyncExportStorage
from api.storage.local.handler.RequestSyncImportStorage import RequestSyncImportStorage
from api.storage.local.handler.RequestUpdateExportStorage import RequestUpdateExportStorage
from api.storage.local.handler.RequestUpdateImportStorage import RequestUpdateImportStorage
from api.storage.local.handler.RequestValidateExportStorage import RequestValidateExportStorage
from api.storage.local.handler.RequestValidateImportStorage import RequestValidateImportStorage

local_storage_api = Blueprint('local_storage_api', __name__)

@local_storage_api.route("/storages/export/localfiles", methods=['POST'])
def create_export_storage():
    api_request = RequestCreateExportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/export/localfiles/validate", methods=['POST'])
def validate_export_storage():
    api_request = RequestValidateExportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/export/localfiles/<file_id>/sync", methods=['POST'])
def sync_export_storage(file_id):
    api_request = RequestSyncExportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/localfiles", methods=['POST'])
def create_import_storage():
    api_request = RequestCreateImportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/localfiles/validate", methods=['POST'])
def validate_import_storage():
    api_request = RequestValidateImportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/localfiles/<file_id>/sync", methods=['POST'])
def sync_import_storage(file_id):
    api_request = RequestSyncImportStorage()
    response = api_request.do()
    return response



@local_storage_api.route("/storages/export/localfiles", methods=['GET'])
def get_all_export_storage():
    api_request = RequestGetAllExportStorage()
    response = api_request.do()
    return response

@local_storage_api.route("/storages/export/localfiles/<file_id>", methods=['GET'])
def get_export_storage(file_id):
    api_request = RequestGetExportStorage(file_id)
    response = api_request.do()
    return response


@local_storage_api.route("/storages/localfiles", methods=['GET'])
def get_all_import_storage():
    api_request = RequestGetAllImportStorage()
    response = api_request.do()
    return response


@local_storage_api.route("/storages/localfiles/<file_id>", methods=['GET'])
def get_import_storage(file_id):
    api_request = RequestGetImportStorage(file_id)
    response = api_request.do()
    return response



@local_storage_api.route("/storages/export/localfiles/<file_id>", methods=['PATCH'])
def update_export_storage(file_id):
    api_request = RequestUpdateExportStorage(file_id)
    response = api_request.do()
    return response

@local_storage_api.route("/storages/localfiles/<file_id>", methods=['PATCH'])
def update_import_storage(file_id):
    api_request = RequestUpdateImportStorage()
    response = api_request.do()
    return response



@local_storage_api.route("/storages/export/localfiles/<file_id>", methods=['DELETE'])
def delete_export_storage(file_id):
    api_request = RequestDeleteExportStorage(file_id)
    response = api_request.do()
    return response

@local_storage_api.route("/storages/localfiles/<file_id>", methods=['DELETE'])
def delete_import_storage(file_id):
    api_request = RequestDeleteImportStorage(file_id)
    response = api_request.do()
    return response