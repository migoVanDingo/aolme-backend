from abc import ABC, abstractmethod
from dao.TableRepoLink import TableRepoLink
from dao.TableRepoItem import TableRepoItem
from dao.TableRepository import TableRepository

class AbstractRepository(ABC):
    
    def __init__(self):
        super().__init__()
        self.repo = TableRepository()
        self.repo_item = TableRepoItem()
        self.repo_link = TableRepoLink()
    
    ###Concrete methods

    #Table Repository
    def create(self, params):
        return self.repo.insert(params)
    
    def read(self, id):
        return self.repo.read(id)
    
    def read_list_owner(self, id):
        return self.repo.read_list_owner(id)
    
    def read_list_entity(self, entity_id):
        return self.repo.read_list_entity(entity_id)
    
    def update(self, params):
        return self.repo.update(params)
    
    def archive(self, id):
        return self.repo.archive(id)
    
    def delete(self, id):
        return self.repo.delete(id)
    

    #Table RepoItem
    def add_repo_item(self, data):
        return self.repo_item.insert(data)
    
    def read_list_repo_items(self, repo_id):
        return self.repo_item.read_list_repo_items(repo_id)
    

    # Table RepoLink
    def add_repo_link(self, data, dir_name):
        return self.repo_link.insert(data, dir_name)
    
    def read_repo_link(self, repo_id):
        return self.repo_link.read(repo_id)
    
    #Abstract methods
    @abstractmethod
    def do_process(self):
        pass