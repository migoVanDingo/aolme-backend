from flask import jsonify
from dao.TableProject import TableProject
from api.project.AbstractProject import AbstractProject


class RequestCreateRepoProject(AbstractProject):
    def __init__(self, data):
        self.data = data

    def do(self):
        
        dao = TableProject()
        result = dao.create_project(self.data) 

        return jsonify(result)
        
        
        

        
       

