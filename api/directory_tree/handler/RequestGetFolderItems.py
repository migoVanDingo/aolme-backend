from datetime import datetime

from flask import current_app
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree  
import os, json
from dotenv import load_dotenv

from dao.TableFilesV2 import TableFilesV2
from dao.TableRepoItem import TableRepoItem
load_dotenv()

class RequestGetFolderItems(AbstractDirectoryTree):
    def __init__(self, entity_id, folder_name, owner_id, repo_id):
        super().__init__()
        self.entity_id = entity_id
        self.folder_name = folder_name
        self.owner_id = owner_id
        self.repo_id = repo_id
        self.path = ""
        self.files_db = TableFilesV2()
        self.repo_item_db = TableRepoItem()

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: entity_id: {self.entity_id} :: folder_name: {self.folder_name} :: owner_id: {self.owner_id} :: repo_id: {self.repo_id}")
            self.path = self.getFolderPath(self.entity_id, self.repo_id, self.folder_name)
            current_app.logger.debug(f"{self.__class__.__name__} :: path: {self.path}")

            current_files = self.files_db.read_list_by_entity(self.entity_id)
            current_app.logger.debug(f"{self.__class__.__name__} :: current_files: {current_files}")

            current_file_names = []
            current_notebooks = []
            for file in current_files:
                current_file_names.append(file['name'])
                if file['type'] == 'NOTEBOOK':
                    current_notebooks.append({ "name": file['name'], "file_id": file['file_id']})
                    
                

            items = []
            with os.scandir(self.path) as it:

                for entry in it:
                    if not entry.name.startswith('.'):
                        if entry.is_file():

                            current_app.logger.debug(f"{self.__class__.__name__} :: FILE: {entry.name}")

                            items.append({ "name": entry.name, "type": self.folder_name.upper()})

                
                            if entry.name not in current_file_names:
                                
                                payload_insert_file = {
                                    "entity_id": self.entity_id,
                                    "name": entry.name,
                                    "description": "Notebook",
                                    "owner": self.owner_id,
                                    "type": "NOTEBOOK",
                                    "created_by": self.owner_id,
                                    "created_at": "{}".format(datetime.now()),
                                    "path": os.path.join(self.path, entry.name),
                                    "is_active": 1,
                                    "is_public": 0,
                                }
                                
                                current_app.logger.debug(f"{self.__class__.__name__} :: PAYLOAD_INSERT_FILE: {payload_insert_file}")
                                response_insert_file = self.files_db.insert_files(payload_insert_file)
                                current_app.logger.debug(f"{self.__class__.__name__} :: RESPONSE_INSERT_FILE: {response_insert_file}")


                                payload_insert_repo_item = {
                                    "file_id": response_insert_file['file_id'],
                                    "repo_id": self.repo_id,
                                    "type": "NOTEBOOK",
                                    "is_active": 1,
                                    "created_at": "{}".format(datetime.now()),
                                    "created_by": self.owner_id
                                }
                                current_app.logger.debug(f"{self.__class__.__name__} :: PAYLOAD_INSERT_REPO_ITEM: {payload_insert_repo_item}")
                                response_repo_item = self.repo_item_db.insert(payload_insert_repo_item)

                                
                                current_app.logger.debug(f"{self.__class__.__name__} :: RESPONSE_INSERT_REPO_ITEM: {response_repo_item}")

                                current_file_names.append(entry.name)

                
            

          
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {items}")

            return items
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
    

    def getFolderPath(self, entity_id, repo_id, folder_name):
        # path = ""
        # if self.entity_id.startswith("ORG"):
        #     path = os.environ['ORGANIZATION_DIRECTORY']
        # elif self.entity_id.startswith("USR"):
        #     path = os.environ['USER_DIRECTORY']



        path = os.path.join(os.environ['REPO_DIRECTORY'], repo_id)
        # path = os.path.join(path, "repo")
        # path = os.path.join(path, repo_id)
        # path = os.path.join(path, "files")
        path = os.path.join(path, folder_name.lower())

        return path

        
    
    
