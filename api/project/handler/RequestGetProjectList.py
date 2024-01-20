from flask import jsonify
from dao.TableProject import TableProject
from api.project.AbstractProject import AbstractProject



class RequestGetProjectList(AbstractProject):
    def __init__(self):
        pass

    def do_process(self):
        dao = TableProject()
        result = dao.get_project_list() 

        return jsonify(result)