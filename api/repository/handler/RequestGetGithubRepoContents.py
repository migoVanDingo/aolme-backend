import os
from api.repository.AbstractRepository  import AbstractRepository
from flask import current_app

from utility.LocalFileManager import LocalFileManager

class RequestGetGithubRepoContents(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: repo_id: {self.repo_id}")

            response = self.read_repo_link(self.repo_id)
            current_app.logger.debug(f"{self.__class__.__name__} :: read repo link: {response}")

            path = os.path.join(response[0]['path'], response[0]['dir_name'])

            response = {
                "repo_id": self.repo_id,
                "path": path,
                "contents": LocalFileManager().get_directory_content(path)
            }

            return response

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetGithubRepoContents -- do_process() Error: " + str(e)