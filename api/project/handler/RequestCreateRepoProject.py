from flask import current_app, jsonify
from dao.TableProject import TableProject
from api.project.AbstractProject import AbstractProject


class RequestCreateRepoProject(AbstractProject):
    def __init__(self, data):
        self.data = data

    def do(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data}")
            dao = TableProject()
            result = dao.create_project(self.data) 
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {result}")
            return jsonify(result)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"
        
        
        
        

        
       

