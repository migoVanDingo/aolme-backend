from flask import current_app
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree

import os
class RequestCreateProjectDirectory(AbstractDirectoryTree):
    
    def __init__(self, org_id, project_id) -> None:
        self.org_id = org_id
        self.project_id = project_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: org_id: {self.org_id} :: project_id: {self.project_id}")
            path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.org_id)
            path = os.path.join(path, 'project')
            path = os.path.join(path, self.project_id)

            if os.path.isdir(path) is True:
                current_app.logger.debug(f"{self.__class__.__name__} :: PROJECT_FOLDER_ALREADY_EXISTS: {path}")
                data = {"message":"PROJECT_FOLDER_ALREADY_EXISTS", "path":path}
                return data
            
            self.create_directory(path)
            
            data = {"message":"PROJECT_FOLDER_CREATED", "path":path}

            current_app.logger.debug(f"{self.__class__.__name__} :: PROJECT_FOLDER_CREATED: {path}")
            return data
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")   
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404