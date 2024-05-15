import os, json, requests
from flask import current_app, jsonify
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree  
from dotenv import load_dotenv
load_dotenv()

class Directory(AbstractDirectoryTree):
    def __init__(self) -> None:
        pass

    def create_directory(self, project_id, folder_name):
        path = os.path.join(os.environ['PROJECT_DIRECTORY'], str(project_id))
        path = os.path.join(path, folder_name)

        if os.path.isdir(path) is True:
            
            current_app.logger.error(f"{self.__class__.__name__} :: FOLDER_ALREADY_EXISTS :: path: {path}")
            data = {"message":"FOLDER_ALREADY_EXISTS", "path":path}
            return data
        

        self.create_directory(path)
        

        
        data = {"message":"FOLDER_CREATED", "path":path}

        current_app.logger.debug(f"{self.__class__.__name__} :: FOLDER_CREATED :: data: {data}")
        return data
    

