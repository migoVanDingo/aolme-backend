from abc import ABC, abstractmethod

from dao.TableModule import TableModule
class AbstractModule(ABC):

    def __init__(self):
        super().__init__()
        self.table_module = TableModule()

    #Concrete methods
    def create(self, params):
        return self.table_module.insert_module(params)
    
    def read_list(self):
        return self.table_module.read_list()
    
    def read_item(self, module_id):
        return self.table_module.read_item(module_id)
    
    def read_list_by_entity(self, entity_id):
        return self.table_module.read_list_by_entity(entity_id)
    
    def read_list_by_user(self, user_id):
        return self.table_module.read_list_by_user(user_id)
    
    def read_list_project(self, project_id):
        return self.table_module.read_list_project(project_id)
    
    def update(self, params):
        return self.table_module.update(params)
    
    def delete(self, module_id):
        return self.table_module.delete(module_id)
    
    def archive(self, module_id):
        return self.table_module.archive(module_id)
    