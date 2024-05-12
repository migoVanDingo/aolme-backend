# from flask import jsonify
# from dao.TableProject import TableProject


# class RequestGetProjectById:
#     def __init__(self, project_id):
#         self.project_id = project_id

#     def do(self):
#         dao = TableProject()
#         result = dao.get_project_by_id(self.project_id) 

#         return jsonify(result)
from flask import current_app
from api.project.AbstractProject import AbstractProject
class RequestGetProjectById(AbstractProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            response = self.get_project_by_id(self.project_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"