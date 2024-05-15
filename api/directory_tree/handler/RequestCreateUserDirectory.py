from flask import current_app
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
import os

from utility.Constant import Constant

class RequestCreateUserDirectory(AbstractDirectoryTree):
    def __init__(self, user_id):
        self.user_id = user_id
    
    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: user_id: {self.user_id}")
            path = os.path.join(os.environ['USER_DIRECTORY'], self.user_id)

            current_app.logger.debug(f"{self.__class__.__name__} :: user-directory-path: {path}")
            
            if os.path.isdir(path) is True:
                
                current_app.logger.error(f"{self.__class__.__name__} :: USER_FOLDER_ALREADY_EXISTS")
                data = {"message":"USER_FOLDER_ALREADY_EXISTS", "path":path}
                return data
            
            self.create_directory(path)

            dir_list = Constant.directory_list
            current_app.logger.debug(f"{self.__class__.__name__} :: directory-list: {dir_list}")

            self.create_dir_list(path, dir_list)

            
            data = {"message":"USER_FOLDER_CREATED", "path":path}
            current_app.logger.debug(f"{self.__class__.__name__} :: user-directory-created: {data}")

            return data
    
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestCreateUserDirectory -- do_process() Error: " + str(e)