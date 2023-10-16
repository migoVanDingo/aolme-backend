import os, json, requests
from flask import jsonify
from dotenv import load_dotenv
load_dotenv()
class Directory:
    def __init__(self) -> None:
        pass

    def create_directory(project_id, folder_name):
        path = os.path.join(os.environ['PROJECT_DIRECTORY'], str(project_id))
        path = os.path.join(path, folder_name)

        if os.path.isdir(path) is True:
            print("FOLDER_ALREADY_EXISTS")
            data = {"message":"FOLDER_ALREADY_EXISTS", "path":path}
            return data
        
    
        os.mkdir(path)
        print("FOLDER_CREATED")
        data = {"message":"FOLDER_CREATED", "path":path}

        print(data)
        return data
