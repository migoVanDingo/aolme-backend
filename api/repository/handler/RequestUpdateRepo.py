from flask import current_app
from api.repository.AbstractRepository import AbstractRepository

class RequestUpdateRepo(AbstractRepository):
    def __init__(self, repo_id, payload):
        super().__init__()
        self.repo_id = repo_id
        self.payload = payload


    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: repo_id: {self.repo_id} :: payload: {self.payload}")
            response = self.update(self.repo_id, self.payload)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"