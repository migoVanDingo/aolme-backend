import os, json
from flask import jsonify
from dotenv import load_dotenv
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
load_dotenv()
class ReadProjectFolder(AbstractDirectoryTree):
    def __init__(self, entity_id, args):
        self.entity_id = entity_id
        self.args = args
        if entity_id.startswith('USR'):
            self.path = "{}/{}".format(os.environ['USER_DIRECTORY'],entity_id)
        elif entity_id.startswith('ORG'):
            self.path = "{}/{}".format(os.environ['ORGANIZATION_DIRECTORY'],entity_id)


    
    def do_process(self):
        #dir_list = os.listdir(self.path)
        #dir_list = os.walk(self.path, topdown=True)

        print('sa: {}'.format(self.args))

        for item in self.args:
            self.path = '{}/{}'.format(self.path, item) 

        print('PATH: {}'.format(self.path))

        response = self.get_folder_items(self.path)
        return response

        

        # items = []
        # with os.scandir(self.path) as it:
        #     for entry in it:
        #         if not entry.name.startswith('.'):
        #             if entry.is_file():
        #                 file_name = entry.name
        #                 base_name, extension = os.path.splitext(file_name)
        #                 items.append({ "name": base_name + extension, "type": "file"})

        #             if entry.is_dir():
        #                 items.append({"name": entry.name, "type": "folder"})
                    
          
            
        #     # Split the file name into base and extension
            

        # print("dir_list: {}".format(items))

