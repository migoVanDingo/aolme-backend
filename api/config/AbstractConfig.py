from abc import ABC, abstractmethod

from dao.TableConfig import TableConfig
class AbstractConfig(ABC):

    def __init__(self):
        super().__init__()
        self.table_config = TableConfig()

    #Concrete methods
    def create(self, params):
        return self.table_config.insert_config(params)
    
    def read_list(self):
        return self.table_config.read_list()
    
    def read_item(self, config_id):
        return self.table_config.read_item(config_id)
    
    def read_item_project(self, project_id):
        return self.table_config.read_item_project(project_id)
    
    def read_list_by_entity(self, entity_id):
        return self.table_config.read_list_by_entity(entity_id)
    
    def read_list_by_user(self, user_id):
        return self.table_config.read_list_by_user(user_id)
    
    def update(self, params):
        return self.table_config.update(params)
    
    def delete(self, config_id):
        return self.table_config.delete(config_id)
    
    def archive(self, config_id):
        return self.table_config.archive(config_id)
    