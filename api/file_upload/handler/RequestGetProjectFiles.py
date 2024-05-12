from flask import current_app
import os, json, requests

from dao.TableFiles import TableFiles
class RequestGetProjectFiles:
    def __init__(self, project_id):
        self.project_id = project_id
    
    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            dao = TableFiles()
            response = dao.get_project_files(self.project_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response 
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        