import os
from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
from api.dataset.handler.RequestCreateDataset import RequestCreateDataset
from api.dataset.handler.RequestCreateSubset import RequestCreateSubset
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject
from api.label_studio.ls_project.handler.RequestCreateLsProject import RequestCreateLsProject
from utility.LocalFileManager import LocalFileManager

""" Example Payload
{
    entity_id = datatypes.String(required=True)
    entity_type = datatypes.String(required=True)
    name= datatypes.String(required=True)
    description = datatypes.String(required=False)
    owner = datatypes.String(required=True)
    type = datatypes.String(required=True)
    is_public = datatypes.Integer(required=True)
    repo_id = datatypes.String(required=True)
} """

class RequestInitializeDatasetRepoLabeler():

    def __init__(self, payload, files):
        super().__init__()
        self.payload = payload
        self.files = files

    # This method is used when user uploads dataset files in the repository
    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__}")

            data = {
                "entity_id": self.payload['entity_id'],
                "entity_type": self.payload['entity_type'],
                "name": self.payload['name'],
                "description": self.payload['description'],
                "owner": self.payload['owner'],
                "type": self.payload['type'],
                "is_public": 0,
                "repo_id": self.payload['repo_id']
                
            }



            # Create the dataset entry in DB
            request_create_dataset = RequestCreateDataset(data, data['repo_id'])
            response_create_dataset = request_create_dataset.do_process()


            # Store files in FS and Create the Subset entry in the DB
            payload_create_subset = self.create_subset_payload(data, response_create_dataset)

            request_create_subset = RequestCreateSubset(payload_create_subset, self.files)
            response_create_subset = request_create_subset.do_process()
    

            # Copy files to the local storage
            #self.move_files_to_local_storage(os.path.join(response_create_subset['path'], "files"), os.path.join(response_create_subset['path'], "local-storage"))

            #Create Label Studio Project
            payload_create_ls_project = self.create_label_studio_payload(data, response_create_subset, response_create_dataset)


            request_create_ls_project = RequestCreateLsProject()
            response_create_ls_project = request_create_ls_project.do_process(payload_create_ls_project)

                           
            
            return self.form_response(response_create_ls_project, response_create_dataset, response_create_subset)

                                                   
                                    
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404                


    def form_response(self, ls, dataset, subset):
        return {
            "ls_project": ls,
            "dataset": dataset,
            "subset": subset
        }


    def move_files_to_local_storage(self, source_path, import_storage_path):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: Move files to local storage :: source_path: {source_path} :: import_storage_path: {import_storage_path}")

            LocalFileManager.move_files(source_path, import_storage_path)

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        
    
    def create_subset_payload(self, data, dataset):
        try:
            subset_path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], data['entity_id'], "dataset", dataset['dataset_id'], "subset") if data['entity_id'].startswith("ORG") else os.path.join(os.environ["USER_DIRECTORY"], data['entity_id'], "dataset", dataset['dataset_id'], "subset")

            payload_create_subset = {
                "name": data['name'] + " subset",
                "description": data['description'] + "Subset of dataset " + data['name'],
                "owner": data['owner'],
                "path": subset_path,
                "isPublic": 0,
                "created_by": data['owner'],
                "dataset_id": dataset['dataset_id'],
                
            }
            return payload_create_subset
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        
    def create_label_studio_payload(self, data, subset, dataset):
        return {
                "name": subset['name'],
                "description": subset['description'],
                "owner": data['owner'],
                "created_by": data['owner'],
                "subset_id": subset['subset_id'],
                "dataset_id": dataset['dataset_id'],
                "entity_id": dataset['entity_id']
            }

        
