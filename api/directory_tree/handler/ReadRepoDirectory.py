from datetime import datetime
import os

from flask import current_app
from api.directory_tree.AbstractDirectoryTree import AbstractDirectoryTree
from dao.TableRepoItem import TableRepoItem
from utility.Constant import Constant

class ReadRepoDirectory(AbstractDirectoryTree):
    def __init__(self, repo_id, entity_id):
        self.repo_id = repo_id
        self.entity_id = entity_id

    
    def do_process(self):

        try:
            current_app.logger.info(f"{self.__class__.__name__} :: repo_id: {self.repo_id} :: entity_id: {self.entity_id}")    

            # all_dir_path = ""
            # if self.entity_id.startswith("ORG"):
            #     all_dir_path = os.path.join(os.environ['ORGANIZATION_DIRECTORY'], self.entity_id)
            # elif self.entity_id.startswith("USR"):
            #     all_dir_path = os.path.join(os.environ['USER_DIRECTORY'], self.entity_id)

            # all_dir_path = os.path.join(all_dir_path, 'repo')
            all_dir_path = os.environ['REPO_DIRECTORY']
            all_dir_path = os.path.join(all_dir_path, self.repo_id)
            #all_dir_path = os.path.join(all_dir_path, 'files')

            dir_list = Constant.directory_list
    
            current_app.logger.info(f"{self.__class__.__name__} :: all_dir_path: {all_dir_path}")
            file_list = []
            for dir in dir_list:
                current_dir = os.path.join(all_dir_path,dir)
                with os.scandir(current_dir) as entries:
                    for entry in entries:
                        if entry.is_file():
                            file_list.append({"name": entry.name, "type": dir.upper()})





            # table_repo_item = TableRepoItem()
            # repo_items = table_repo_item.read_list_repo_items(self.repo_id)

            current_app.logger.info(f"{self.__class__.__name__} :: Response: {file_list}")
            
            return file_list
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404