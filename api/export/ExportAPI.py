from flask import Blueprint, request
import json
from api.export.handler.RequestConvertExportSnapshotToFormat import RequestConvertExportSnapshotToFormat
from api.export.handler.RequestCreateNewExportSnapshot import RequestCreateNewExportSnapshot
from api.export.handler.RequestDeleteExportSnapshot import RequestDeleteExportSnapshot
from api.export.handler.RequestDownloadExportInSpecifiedFormat import RequestDownloadExportInSpecifiedFormat

from api.export.handler.RequestExportTasksAndAnnotations import RequestExportTasksAndAnnotations
from api.export.handler.RequestGetExportFormats import RequestGetExportFormats
from api.export.handler.RequestGetExportSnapshotById import RequestGetExportSnapshotById
from api.export.handler.RequestListAllExportSnapshots import RequestListAllExportSnapshots

export_api = Blueprint('export_api', __name__)

#Easy export tasks & annotations
@export_api.route("/export/projects/<project_id>", methods=['GET'])
def export_tasks_and_annotations(project_id):
    api_request = RequestExportTasksAndAnnotations(project_id)
    response = api_request.do()
    return response


#Get Export formats for project
@export_api.route('/export/projects/<project_id>/formats', method=['GET'])
def get_export_formats(project_id):
    api_request = RequestGetExportFormats(project_id)
    response = api_request.do()
    return response


#Get list all export snapshots
@export_api.route("/projects/<project_id>/exports", method=['GET'])
def list_all_export_snapshots(project_id):
    api_request = RequestListAllExportSnapshots(project_id)
    response = api_request.do()
    return response


#Get Download export snapshot as file in specific format
@export_api.route("/projects/<project_id>/exports/<export_key>/download", methods=['GET'])
def download_export_file_specific_format(project_id, export_key):
    api_request = RequestDownloadExportInSpecifiedFormat(project_id, export_key)
    response = api_request.do()
    return response


#Get export snapshot by ID
@export_api.route("/projects/<project_id>/exports/<export_key>", methods=['GET'])
def get_export_snapshot_by_id(project_id, export_key):
    api_request = RequestGetExportSnapshotById(project_id, export_key)
    response = api_request.do()
    return response


#Create new export snapshot
@export_api.route("/projects/<project_id>/exports", method=["POST"])
def create_new_export_snapshot(project_id):
    api_request = RequestCreateNewExportSnapshot(project_id)
    response = api_request.do()
    return response


#Convert export snapshot to specific format
@export_api.route('/projects/<project_id>/exports/<export_key>/convert', methods=['POST'])
def export_conversion(project_id, export_key):
    api_request = RequestConvertExportSnapshotToFormat(project_id, export_key)
    response = api_request.do()
    return response

#Delete snapshot
@export_api.route('/projects/<project_id>/exports/<export_key>', methods=['DELETE'])
def delete_export_snapshot(project_id, export_key):
    api_request = RequestDeleteExportSnapshot(project_id, export_key)
    response = api_request.do()
    return response