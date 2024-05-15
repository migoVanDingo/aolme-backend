import os, json
from flask import current_app, jsonify
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
        try:
            #dir_list = os.listdir(self.path)
            #dir_list = os.walk(self.path, topdown=True)
            current_app.logger.debug(f"{self.__class__.__name__} :: entity_id: {self.entity_id}")
            current_app.logger.debug(f"{self.__class__.__name__} :: args: {self.args}")


            for item in self.args:
                self.path = '{}/{}'.format(self.path, item) 

 
            current_app.logger.debug(f"{self.__class__.__name__} :: path: {self.path}")

            response = self.get_folder_items(self.path)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        
        


