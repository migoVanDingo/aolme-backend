from flask import current_app, jsonify
from dao.TableProject import TableProject
from api.project.AbstractProject import AbstractProject



class RequestGetProjectList(AbstractProject):
    def __init__(self):
        pass

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__}:: RequestGetProjectList")
            dao = TableProject()
            result = dao.get_project_list() 
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {result}") 
            return jsonify(result)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"