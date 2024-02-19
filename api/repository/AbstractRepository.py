from abc import ABC, abstractmethod
from dao.TableRepoItem import TableRepoItem
from dao.TableRepository import TableRepository

class AbstractRepository(ABC):
    
    def __init__(self):
        super().__init__()
        self.repo = TableRepository()
    
    #Concrete methods
    def create(self, params):
        return self.repo.insert(params)
    
    def read(self, id):
        return self.repo.read(id)
    
    def read_list_owner(self, id):
        return self.repo.read_list_owner(id)
    
    def read_list_entity(self, entity_id):
        return self.repo.read_list_entity(entity_id)
    
    def read_list_repo_items(self, repo_id):
        repo_item = TableRepoItem()
        return repo_item.read_list_repo_items(repo_id)
    
    def update(self, params):
        return self.repo.update(params)
    
    def archive(self, id):
        return self.repo.archive(id)
    
    def delete(self, id):
        return self.repo.delete(id)
    
    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass