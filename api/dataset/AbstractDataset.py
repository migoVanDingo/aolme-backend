from abc import ABC, abstractmethod

from dao.TableFilesV2 import TableFilesV2
from dao.TableDatasetV2 import TableDatasetV2
from dao.TableSubset import TableSubset
from dao.TableSubsetItem import TableSubsetItem
class AbstractDataset(ABC):

    def __init__(self):
        super().__init__()
        self.table_dataset = TableFilesV2()
        self.v2 = TableDatasetV2()
        self.subset = TableSubset()
        self.subset_item = TableSubsetItem()

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
    

    #Subset API
    def create_subset(self, params):
        return self.subset.insert(params)
    
    def read_subset(self, subset_id):
        return self.subset.read_item(subset_id)
    
    def read_list_by_dataset_id(self, dataset_id):
        return self.subset.read_list_by_dataset_id(dataset_id)
    
    
    #Subset Item API
    def create_subset_item(self, params):
        return self.subset_item.insert(params)
    
    def read_subset_item(self, subset_item_id):
        return self.subset_item.read_item(subset_item_id)
    
    def read_items_by_subset_id(self, subset_id):
        return self.subset_item.read_list(subset_id)
    
    def read_items_by_subset_and_filename(self, subset_id, filename):
        return self.subset_item.read_item_by_subset_and_filename(subset_id, filename)
    