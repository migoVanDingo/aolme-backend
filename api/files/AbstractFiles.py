from abc import ABC, abstractmethod

from dao.TableFiles import TableFiles

class AbstractFiles(ABC):
    def __init__(self, path):
        self.path = path

    def insert_file(self, file_name, file_content):
        return TableFiles().insert_file(file_name, file_content)
    
    def read_file(self, file_name):
        return TableFiles().read_file(file_name)

    def update_file_info(self, file_name, file_content):
        return TableFiles().update_file_info(file_name, file_content)

    def delete_file(self, file_name):
        return TableFiles().delete_file(file_name)
    
    def archive_file(self, file_name):
        return TableFiles().archive_file(file_name)

    @abstractmethod
    def do_process(self):
        pass