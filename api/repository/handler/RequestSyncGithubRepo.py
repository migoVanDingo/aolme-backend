from flask import current_app
from api.repository.AbstractRepository import AbstractRepository
from utility.GitUtility import GitUtility

class RequestSyncGithubRepo(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: repo_id: {self.repo_id}")

            dir_name = self.read_repo_link(self.repo_id)[0]['dir_name']

            current_app.logger.debug(f"{self.__class__.__name__} :: dir_name: {dir_name}")

            response = GitUtility().sync_repo(self.repo_id, dir_name)
            current_app.logger.debug(f"{self.__class__.__name__} :: Github Sync Repo: {self.repo_id}")
            return response
        except Exception as e:
            return "RequestSyncGithubRepo -- do_process() Error: " + str(e)