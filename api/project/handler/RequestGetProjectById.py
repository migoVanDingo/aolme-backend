# from flask import jsonify
# from dao.TableProject import TableProject


# class RequestGetProjectById:
#     def __init__(self, project_id):
#         self.project_id = project_id

#     def do(self):
#         dao = TableProject()
#         result = dao.get_project_by_id(self.project_id) 

#         return jsonify(result)
from api.project.AbstractProject import AbstractProject
class RequestGetProjectById(AbstractProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        print("here boi")
        return self.get_project_by_id(self.project_id)