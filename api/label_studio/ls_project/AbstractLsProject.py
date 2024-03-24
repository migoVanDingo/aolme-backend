from abc import ABC, abstractmethod
import os, json
import requests
from dotenv import load_dotenv

from dao.TableLsProject import TableLsProject
load_dotenv()


class AbstractLsProject(ABC):
    def __init__(self):
        super().__init__()
        self.dao = TableLsProject()
        self.token=os.environ['LABEL_STUDIO_USER_TOKEN']

    def get_token(self):
        return os.environ['LABEL_STUDIO_USER_TOKEN']

    def get_headers(self):
        headers = {
            "Authorization":"Token {}".format(self.get_token()),
            "Content-Type": "application/json"
        }
        print("Headers: {}".format(headers))
        return headers
    
    def get_webhook_headers(self):
        webhook_headers = {
            "Authorization":"Token {}".format(self.get_token())
        }
        print("Webhook Headers: {}".format(webhook_headers))
        return webhook_headers


    def endpoint_url_create_ls_project(self):
        return "http://localhost:8080/api/projects"
    
    def endpoint_url_create_webhook(self):
        return "http://localhost:8080/api/webhooks"
    
    def endpoint_url_get_project_list(self):
        return "http://localhost:8080/api/projects"
    
    def endpoint_url_get_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_url_update_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_url_delete_ls_project(self, ls_project_id):
        return "http://localhost:8080/api/projects/{}".format(ls_project_id)
    
    def endpoint_validate_label_config(self):
        return "http://localhost:8080/api/projects/validate"
    
    def endpoint_url_create_import_storage(self):
        return "http://localhost:8080/api/storages/localfiles"
    
    def endpoint_url_sync_imoport_storage(self, local_storage_id):
        return "http://localhost:8080/api/storages/localfiles/{}/sync".format(local_storage_id)
    
    def endpoint_url_get_all_frames(self, project_id):
        return "http://localhost:8080/api/projects/"+ str(project_id) +"/export?exportType=JSON&interpolate_key_frames=true"
    




    #Requests
    def post(self, url, payload, headers):
        return requests.post(url, data=payload, headers=headers)
    
    def get(self, url, headers):
        return requests.get(url, headers=headers)
    
    def patch(self, url, payload, headers):
        return requests.patch(url, data=payload, headers=headers)
    
    def delete(self, url, headers):
        return requests.delete(url, headers=headers)



    # Interact with Label Studio
    def create_ls_project(self, payload):
        return self.post(self.endpoint_url_create_ls_project(), payload, self.get_headers()).json()

    def get_ls_project_list(self):
        return self.get(self.endpoint_url_get_project_list(), self.get_headers())

    def get_ls_project(self, ls_project_id):
        return self.get(self.endpoint_url_get_ls_project(ls_project_id), self.get_headers())

    def update_ls_project(self, ls_project_id, payload):
        return self.patch(self.endpoint_url_update_ls_project(ls_project_id), payload, self.get_headers())

    def delete_ls_project(self, ls_project_id):
        return self.delete(self.endpoint_url_delete_ls_project(ls_project_id), self.get_headers())

    def validate_label_config(self, config):
        return self.post(self.endpoint_validate_label_config(), config, self.get_headers())
    
    def create_webhook(self, payload):
        return self.post(self.endpoint_url_create_webhook(), payload, headers=self.get_webhook_headers())
    
    def create_import_storage(self, payload):
        return self.post(self.endpoint_url_create_import_storage(), payload, self.get_headers())
    
    def sync_import_storage(self, local_storage_id, payload):
        return self.post(self.endpoint_url_sync_imoport_storage(local_storage_id), payload, self.get_headers())





    # Persist to database
    def insert_ls_project(self, payload):
        return self.dao.insert_ls_project(payload)

    def get_ls_project_by_id(self, ls_project_id):
        return self.dao.read_ls_project_by_id(ls_project_id)

    def get_ls_project_list_by_entity_id(self, entity_id):
        return self.dao.read_ls_project_list_by_entity_id(entity_id)
    
    def get_ls_project_by_repo_id(self, repo_id):
        return self.dao.read_ls_project_by_repo_id(repo_id)

    def get_ls_project_list_by_dataset_id(self, dataset_id):
        return self.dao.read_ls_project_list_by_dataset_id(dataset_id)

    def update_ls_project(self, ls_project_id, payload):
        return self.dao.update_ls_project(ls_project_id, payload)

    def archive_ls_project(self, ls_project_id):
        return self.dao.archive_ls_project(ls_project_id)

    def delete_ls_project(self, ls_project_id):
        return self.dao.delete_ls_project(ls_project_id)



    


    @abstractmethod
    def do_process(self):
        pass