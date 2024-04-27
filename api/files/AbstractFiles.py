from abc import ABC, abstractmethod
from dao.TableFilesV2 import TableFilesV2

class AbstractFiles(ABC):
    def __init__(self):
        super().__init__()
        self.db = TableFilesV2()

    def insert_file(self, payload):
        return self.db.insert_files(payload)
    
    def read_file(self, file_name):
        return self.db.read_item(file_name)
    
    def read_files(self):
        return self.db.read_list()
    
    def read_files_by_entity(self, entity_id):
        return self.db.read_list_by_entity(entity_id)
    
    def read_files_by_user(self, user_id):
        return self.db.read_list_by_user(user_id)

    def update_file_info(self, file_name, file_content):
        return self.db.update(file_name, file_content)

    def delete_file(self, file_name):
        return self.db.delete(file_name)
    
    def archive_file(self, file_name):
        return self.db.archive(file_name)

    @abstractmethod
    def do_process(self):
        pass