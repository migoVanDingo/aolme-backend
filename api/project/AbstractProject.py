from abc import ABC, abstractmethod

from dao.TableProject import TableProject

class AbstractProject(ABC):
        
        def __init__(self):
            super().__init__()
        
        #Concrete methods
        def insert_project(params):
            return TableProject.insert_project(params)
        
        def read_project(self, project_id):
             return TableProject.read_project(project_id)
              
        def update_project(self, params):
            return TableProject.update_project(params)
    
        def archive_project(self, project_id):
            return TableProject.archive_project(project_id)
    
        def delete_project(self, project_id):
            return TableProject.delete_project(project_id)
    
        #Abstract methods
        @abstractmethod
        def do_process(self):
            pass