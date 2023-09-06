import os, json, requests

from dao.TableFiles import TableFiles
class RequestGetProjectFiles:
    def __init__(self, project_id):
        self.project_id = project_id
    
    def do(self):
        response = TableFiles.get_project_files(self.project_id)

        return response 
        