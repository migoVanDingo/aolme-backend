from abc import ABC, abstractmethod
from dao.TableRepository import TableRepository

class AbstractRepository(ABC):
    
    def __init__(self):
        super().__init__()
        self.db = TableRepository()
    
    #Concrete methods
    def create(self, params):
        return self.db.insert(params)
    
    def read(self, id):
        return self.db.read(id)
    
    def read_list_owner(self):
        return self.db.read_list_owner()
    
    def read_list_entity(self, entity_id):
        return self.db.read_list_entity(entity_id)
    
    def update(self, params):
        return self.db.update(params)
    
    def archive(self, id):
        return self.db.archive(id)
    
    def delete(self, id):
        return self.db.delete(id)
    
    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass