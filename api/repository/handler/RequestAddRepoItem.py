from flask import current_app
from api.repository.AbstractRepository import AbstractRepository

class RequestAddRepoItem(AbstractRepository):
    def __init__(self, repo_id, data):
        super().__init__()
        self.repo_id = repo_id
        self.data = data

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: repo_id: {self.repo_id} :: payload: {self.data}")
            payload = {
                "file_id": self.data['file_id'],
                "repo_id": self.repo_id,
                "type": self.data['file_type'],
                "user_id": self.data['user_id'],
            }

            current_app.logger.debug(f"{self.__class__.__name__} :: add-repo-item-payload: {payload}")
            response = self.add_repo_item(payload)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestAddRepoItem -- do_process() Error: " + str(e)