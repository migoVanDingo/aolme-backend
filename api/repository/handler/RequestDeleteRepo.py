from flask import current_app
from api.repository.AbstractRepository import AbstractRepository
class RequestDeleteRepo(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id


    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: repo_id: {self.repo_id}")
            return self.delete(self.repo_id)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"