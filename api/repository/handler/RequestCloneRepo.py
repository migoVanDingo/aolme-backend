import os
from api.repository.AbstractRepository import AbstractRepository
from utility.GitUtility import GitUtility
from flask import current_app

class RequestCloneRepo(AbstractRepository):
    def __init__(self, data):
        super().__init__()
        self.data = data

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.data}")
            dir_name = GitUtility().clone(self.data['github_url'], self.data['repo_id'], self.data['entity_id'])

            self.data['type'] = 'GITHUB'
            self.data['path'] = os.path.join(os.environ['REPO_DIRECTORY'], self.data['repo_id'], 'project')

            response = self.add_repo_link(self.data, dir_name)
            current_app.logger.debug(f"{self.__class__.__name__} :: Github Linked to Repo: {self.data}")
            return response
        except Exception as e:
            return "RequestCloneRepo -- do_process() Error: " + str(e)