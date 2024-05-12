
from flask import current_app
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
import os

from utility.Constant import Constant
class RequestCreateOrganizationDirectory(AbstractDirectoryTree):
    def __init__(self, org_id) -> None:
        self.org_id = org_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: org_id: {self.org_id}")
            path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.org_id)

            if os.path.isdir(path) is True:
                current_app.logger.info(f"{self.__class__.__name__} :: FOLDER_ALREADY_EXISTS: {path}")
                data = {"message":"FOLDER_ALREADY_EXISTS", "path":path}
                return data
            
            self.create_directory(path)

            dir_list = Constant.directory_list

            self.create_dir_list(path, dir_list)
            
            current_app.logger.info(f"{self.__class__.__name__} :: ORG_FOLDER_CREATED: {path}")
            data = {"message":"ORG_FOLDER_CREATED", "path":path}

   
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404