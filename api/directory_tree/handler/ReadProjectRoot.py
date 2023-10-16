import os, json
from flask import jsonify
from dotenv import load_dotenv
load_dotenv()
class ReadProjectRoot:
    def __init__(self, project_id):
        self.project_id = project_id
        self.path = "{}/{}".format(os.environ['PROJECT_DIRECTORY'],project_id)
    
    def do(self):
        #dir_list = os.listdir(self.path)
        #dir_list = os.walk(self.path, topdown=True)
        items = []
        with os.scandir(self.path) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_file():
                        file_name = entry.name
                        base_name, extension = os.path.splitext(file_name)
                        items.append({ "name": base_name + extension, "type": "file"})

                    if entry.is_dir():
                        items.append({"name": entry.name, "type": "folder"})
                    
          
            
            # Split the file name into base and extension
            

        print("dir_list: {}".format(items))

        return items

