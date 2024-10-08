import os

from flask import current_app
from api.repository.AbstractRepository import AbstractRepository
from datetime import datetime

from utility.Constant import Constant
from utility.GitUtility import GitUtility
class RequestCreateRepo(AbstractRepository):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload


    def do_process(self):
        try:
            self.payload["created_at"] = f"{datetime.now()}"
            self.payload["is_active"] = True

            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")


            response = self.create(self.payload)

            repo_directory = os.path.join(os.environ['REPO_DIRECTORY'],response['repo_id'])
            current_app.logger.debug(f"{self.__class__.__name__} :: repo-directory: {repo_directory}")
            os.mkdir(repo_directory)
            # repo_directory = os.path.join(user_directory, 'repo')
            # repo_directory = os.path.join(repo_directory, response['repo_id'])
            # 
            # repo_dir_files = os.path.join(repo_directory,'files')
            # os.mkdir(repo_dir_files)

            dir_list = Constant.directory_list

            for dir in dir_list:
                os.mkdir(os.path.join(repo_directory,dir))

            GitUtility().git_init(repo_directory)

            current_app.logger.debug(f"{self.__class__.__name__} :: repo-directory-created: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestCreateRepo -- do_process() Error: " + str(e)

        