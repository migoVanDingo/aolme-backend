import json
import os
import shutil
from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
from api.dataset.handler.RequestGetLabelStudioProject import RequestGetLabelStudioProject
from api.label_studio.ls_project.handler.RequestSyncImportStorage import RequestSyncImportStorage
from dao.TableSubsetItem import TableSubsetItem

class RequestPushToSubset(AbstractDataset):
    def __init__(self, params, files):
        super().__init__()
        self.params = params
        self.files = files

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: params: {self.params}")

            subset_id = self.params['subset_id']
            path = self.params['path']


            label_studio_project = self.check_subset_ls_project(subset_id)

            if label_studio_project is None:
                return f"{self.__class__.__name__} :: ERROR: Label Studio Project not found", 404
            
       
            

            #Save uploaded files
            self.save_files(subset_id, self.files, path)

            import_id = label_studio_project['ls_import_id']
            project_id = label_studio_project['ls_project_id']
            import_storage_path = label_studio_project["path"]

            current_app.logger.debug(f"{self.__class__.__name__} :: files saved successfully2")

            # Move files to local-storage directory
            self.move_files(os.path.join(path, "files"), import_storage_path)

            current_app.logger.debug(f"{self.__class__.__name__} :: files moved successfully")

            payload_sync_import_storage = {
                "project": project_id,
                "use_blob_urls": True
            }

            api_request = RequestSyncImportStorage(import_id, payload_sync_import_storage)
            sync_response = api_request.do_process()

            current_app.logger.debug(f"{self.__class__.__name__} :: sync_response: {sync_response}")
    

            return "FILES_MOVED"
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        
    
    def check_subset_ls_project(self, subset_id):
        dao_request = RequestGetLabelStudioProject(subset_id)
        return dao_request.do_process()
    
    def move_files(self, files_path, import_storage_path):
        for file in os.listdir(files_path):
            shutil.copyfile(os.path.join(files_path, file), os.path.join(import_storage_path, file))
    
    
    def save_files(self, subset_id, files, path):
        
        for file in files:
            f = file.filename

            name = f.split('.')
            extension = name[1]

            file_save_payload = {
                "subset_id": subset_id,
                "created_by": self.params['owner'], 
                    
            }


            if extension == "xlsx":
                filepath = os.path.join(path, "xlsx")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "XLSX"
                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                self.create_subset_item(file_save_payload)
                file.save(os.path.join(filepath, f))

            
            elif extension == "json" or extension == "txt" or extension == "csv":

                filepath = os.path.join(path, "annotation")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "ANNOTATION"
                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                self.create_subset_item(file_save_payload)
                file.save(os.path.join(filepath, f))



            elif extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif":
                
                filepath = os.path.join(path, "files")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "IMAGE"
                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                file.save(os.path.join(filepath, f))
                self.create_subset_item(file_save_payload)

            elif  extension == "mp4" or extension == "mov" or extension == "mpg":
                filepath = os.path.join(path, "files")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "VIDEO"
                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                file.save(os.path.join(filepath, f))
                self.create_subset_item(file_save_payload)

        

            elif extension == "mp3" or extension == "wav": 
                filepath = os.path.join(path, "files")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "AUDIO"

                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                file.save(os.path.join(filepath, f))
                self.create_subset_item(file_save_payload)

            else:
                filepath = os.path.join(path, "misc")
                file_save_payload['path'] = filepath
                file_save_payload['name'] = f
                file_save_payload["type"] = "MISC"
                current_app.logger.debug(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                file.save(os.path.join(filepath, f))    
                self.create_subset_item(file_save_payload)               
        

        current_app.logger.debug(f"{self.__class__.__name__} :: files saved successfully")