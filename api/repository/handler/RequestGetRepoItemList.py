from flask import current_app, jsonify
from api.repository.AbstractRepository import AbstractRepository

class RequestGetRepoItemList(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: repo_id: {self.repo_id}")
            response = jsonify(self.read_list_repo_items(self.repo_id))
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetRepoItemList -- do_process() Error: " + str(e)