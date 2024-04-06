from abc import ABC, abstractmethod

from dao.TableLocalStorage import TableImportStorage, TableLocalStorage

class AbstractLocalStorage(ABC):
    def __init__(self):
        pass

    # Export storage
    def create_export_storage(self):
        pass

    def get_export_storage(self):
        pass

    def update_export_storage(self):
        pass

    def validate_export_storage(self):
        pass

    def sync_export_storage(self):
        pass

    def delete_export_storage(self):
        pass


    # Import storage
    def create_import_storage(self):
        pass

    def get_import_storage(self):
        pass

    def update_import_storage(self):
        pass

    def validate_import_storage(self):
        pass

    def sync_import_storage(self):
        pass

    def delete_import_storage(self):
        pass


    # Interact with database
    def insert_import_storage_settings(self, payload):
        return TableLocalStorage.insert_import_storage(payload)

    def read_import_storage_settings(self, project_id):
        return TableLocalStorage.read_import_storage(project_id)   

    def update_import_storage_settings(self, project_id, payload):    
        return TableLocalStorage.update_import_storage(project_id, payload)

    def delete_import_storage_settings(self, project_id):
        return TableLocalStorage.delete_import_storage(project_id)




    def insert_export_storage(self, payload):
        return TableLocalStorage.insert_export_storage(payload)

    def get_export_storage(self, project_id):
        return TableLocalStorage.read_export_storage(project_id)    

    def update_export_storage(self, project_id, payload):    
        return TableLocalStorage.update_export_storage(project_id, payload)

    def delete_export_storage(self, project_id):
        return TableLocalStorage.delete_export_storage(project_id)



         