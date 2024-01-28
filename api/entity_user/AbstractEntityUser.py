from abc import ABC, abstractmethod

from dao.TableEntityUser import TableEntityUser

class AbstractEntityUser(ABC):
    
    def __init__(self):
        super().__init__()
        self.table_entity_user = TableEntityUser()

    #Concrete methods
    def create_entity_user(self, params):
        return self.table_entity_user.insert_entity_user(params)
    
    def get_entity_list_by_user_id(self, user_id):
        return self.table_entity_user.read_entity_list_by_user_id(user_id)
    
    def get_user_list_by_entity_id(self, entity_id):
        return self.table_entity_user.read_user_list_by_entity_id(entity_id)

    def update_entity_user(self, params):
        return self.table_entity_user.update_entity_user(params)

    def archive_entity_user(self, entity_user_id):
        return self.table_entity_user.archive_entity_user(entity_user_id)

    def delete_entity_user(self, entity_user_id):
        return self.table_entity_user.delete_entity_user(entity_user_id)

    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass