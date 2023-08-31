from flask import jsonify
from dao.TableProject import TableProject


class RequestGetProjectList:
    def __init__(self):
        pass

    def do(self):
        dao = TableProject()
        result = dao.get_project_list() 

        return jsonify(result)