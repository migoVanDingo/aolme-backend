from abc import ABC, abstractmethod

from dao.TableDataset import TableDataset
from dao.TableDatasetV2 import TableDatasetV2
class AbstractDataset(ABC):

    def __init__(self):
        super().__init__()
        self.table_dataset = TableDataset()
        self.v2 = TableDatasetV2()

    #Concrete methods
    def create(self, params):
        return self.v2.insert(params)
    
    def read_list(self):
        return self.table_dataset.read_list()
    
    def read_item(self, dataset_id):
        return self.v2.read_item(dataset_id)
    
    def read_list_by_entity(self, entity_id):
        return self.v2.read_list_entity(entity_id)
    
    def read_list_by_user(self, user_id):
        return self.table_dataset.read_list_by_user(user_id)
    
    def update(self, params):
        return self.table_dataset.update(params)
    
    def delete(self, dataset_id):
        return self.table_dataset.delete(dataset_id)
    
    def archive(self, dataset_id):
        return self.table_dataset.archive(dataset_id)
    