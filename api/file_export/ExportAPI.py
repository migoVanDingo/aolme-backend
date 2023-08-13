from flask import Blueprint, request
import json
from api.file_export.handler.RequestConvertExportSnapshotToFormat import RequestConvertExportSnapshotToFormat
from api.file_export.handler.RequestCreateNewExportSnapshot import RequestCreateNewExportSnapshot
from api.file_export.handler.RequestDeleteExportSnapshot import RequestDeleteExportSnapshot
from api.file_export.handler.RequestDownloadExportInSpecifiedFormat import RequestDownloadExportInSpecifiedFormat

from api.file_export.handler.RequestExportTasksAndAnnotations import RequestExportTasksAndAnnotations
from api.file_export.handler.RequestGetExportFormats import RequestGetExportFormats
from api.file_export.handler.RequestGetExportSnapshotById import RequestGetExportSnapshotById
from api.file_export.handler.RequestListAllExportSnapshots import RequestListAllExportSnapshots

file_export_api = Blueprint('file_export_api', __name__)

#Easy export tasks & annotations
@file_export_api.route("/export/projects/<project_id>", methods=['GET'])
def export_tasks_and_annotations(project_id):
    api_request = RequestExportTasksAndAnnotations()
    response = api_request.do()
    return response


#Get Export formats for project
@file_export_api.route('/export/projects/<project_id>/formats', methods=['GET'])
def get_export_formats(project_id):
    api_request = RequestGetExportFormats()
    response = api_request.do()
    return response


#Get list all export snapshots
@file_export_api.route("/projects/<project_id>/exports", methods=['GET'])
def list_all_export_snapshots(project_id):
    api_request = RequestListAllExportSnapshots()
    response = api_request.do()
    return response


#Get Download export snapshot as file in specific format
@file_export_api.route("/projects/<project_id>/exports/<export_key>/download", methods=['GET'])
def download_export_file_specific_format(project_id, export_key):
    api_request = RequestDownloadExportInSpecifiedFormat()
    response = api_request.do()
    return response


#Get export snapshot by ID
@file_export_api.route("/projects/<project_id>/exports/<export_key>", methods=['GET'])
def get_export_snapshot_by_id(project_id, export_key):
    api_request = RequestGetExportSnapshotById()
    response = api_request.do()
    return response


#Create new export snapshot
@file_export_api.route("/projects/<project_id>/exports", methods=["POST"])
def create_new_export_snapshot(project_id):
    api_request = RequestCreateNewExportSnapshot()
    response = api_request.do()
    return response


#Convert export snapshot to specific format
@file_export_api.route('/projects/<project_id>/exports/<export_key>/convert', methods=['POST'])
def export_conversion(project_id, export_key):
    api_request = RequestConvertExportSnapshotToFormat()
    response = api_request.do()
    return response

#Delete snapshot
@file_export_api.route('/projects/<project_id>/exports/<export_key>', methods=['DELETE'])
def delete_export_snapshot(project_id, export_key):
    api_request = RequestDeleteExportSnapshot()
    response = api_request.do()
    return response