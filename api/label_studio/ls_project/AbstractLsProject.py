from abc import ABC, abstractmethod
import os
import requests
from dotenv import load_dotenv

from dao.TableLsProject import TableLsProject
load_dotenv()


class AbstractLsProject(ABC):
    def __init__(self):
        self.token=os.environ['LABEL_STUDIO_SECRET_KEY']
        self.headers = {
            "Authorization":"Token {}".format(self.token),
            "Content-Type": "application/json"
        }


    def endpoint_url_create_ls_project(self):
        return "http://localhost:8080/api/projects/"
    
    def endpoint_url_get_project_list(self):
        return "http://localhost:8080/api/projects/"
    
    def endpoint_url_get_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_url_update_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_url_delete_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_validate_label_config(self):
        return "http://localhost:8080/api/projects/validate"
    




    #Requests
    def post(self, url, payload):
        return requests.post(url, data=payload, headers=self.headers)
    
    def get(self, url):
        return requests.get(url, headers=self.headers)
    
    def patch(self, url, payload):
        return requests.patch(url, data=payload, headers=self.headers)
    
    def delete(self, url):
        return requests.delete(url, headers=self.headers)



    # Interact with Label Studio
    def create_ls_project(self, payload):
        return self.post(self.endpoint_url_create_ls_project(), payload)

    def get_ls_project_list(self):
        return self.get(url=self.endpoint_url_get_project_list())

    def get_ls_project(self, ls_project_id):
        return self.get(url=self.endpoint_url_get_ls_project(ls_project_id))

    def update_ls_project(self, ls_project_id, payload):
        return self.patch(self.endpoint_url_update_ls_project(ls_project_id), payload)

    def delete_ls_project(self, ls_project_id):
        return self.delete(self.endpoint_url_delete_ls_project(ls_project_id))

    def validate_label_config(self, config):
        return self.post(self.endpoint_validate_label_config(), config)




    # Persist to database
    def insert_ls_project(self, payload):
        return TableLsProject.insert_ls_project(payload)

    def get_ls_project_by_id(self, ls_project_id):
        return TableLsProject.read_ls_project_by_id(ls_project_id)

    def get_ls_project_list_by_entity_id(self, entity_id):
        return TableLsProject.read_ls_project_list_by_entity_id(entity_id)

    def get_ls_project_list_by_dataset_id(self, dataset_id):
        return TableLsProject.read_ls_project_list_by_dataset_id(dataset_id)

    def update_ls_project(self, ls_project_id, payload):
        return TableLsProject.update_ls_project(ls_project_id, payload)

    def archive_ls_project(self, ls_project_id):
        return TableLsProject.archive_ls_project(ls_project_id)

    def delete_ls_project(self, ls_project_id):
        return TableLsProject.delete_ls_project(ls_project_id)



    


    @abstractmethod
    def do_process(self):
        pass