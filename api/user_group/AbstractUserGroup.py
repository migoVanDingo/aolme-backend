from abc import ABC, abstractmethod

from dao.TableUserGroup import TableUserGroup

class AbstractUserGroup(ABC):
    def __init__(self, path):
        self.path = path

    def insert_user_group(self, params):
        return TableUserGroup().insert_user_group(params)
    
    def read_user_group(self, user_group_id):
        return TableUserGroup().read_user_group(user_group_id)
    
    def update_user_group(self, params):
        return TableUserGroup().update_user_group(params)
    
    def delete_user_group(self, user_group_id):
        return TableUserGroup().delete_user_group(user_group_id)
    
    def archive_user_group(self, user_group_id):
        return TableUserGroup().archive_user_group(user_group_id)
    

    @abstractmethod
    def do_process(self):
        pass