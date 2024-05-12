import os

from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
from api.file_upload.FileUtility import FileUtility
from api.label_studio.storage.local.handler.RequestSyncImportStorage import RequestSyncImportStorage
from api.subprocess.handler.HandleUploadGroundTruthLabelStudio import HandleUploadGroundTruthLabelStudio
from dao.TableLsImportStorage import TableLsImportStorage

class RequestSyncLabelStudioFiles(AbstractDataset):
    def __init__(self,data, file_set_id = None):
        super().__init__()
        self.data = data
        self.file_set_id = file_set_id
        
    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data} :: file_set_id: {self.file_set_id}")
            data = self.data

            dao_import_storage = TableLsImportStorage()
            import_storage = dao_import_storage.read_ls_import_storage_by_subset_id(data['subset_id'])

            current_app.logger.info(f"{self.__class__.__name__} :: read_ls_import_storage_by_subset_id: {import_storage}")

            path = ""
            if(data['entity_id'].startswith("ORG")):
                path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], data['entity_id'], "dataset", data['dataset_id'], "subset", data['subset_id'])
            elif(data['entity_id'].startswith("USR")):
                path = os.path.join(os.environ["USER_DIRECTORY"], data['entity_id'], "dataset", data['dataset_id'], "subset", data['subset_id'])
            else:
                current_app.logger.error(f"{self.__class__.__name__} :: Invalid entity_id: {data['entity_id']}")
                return "RequestSyncLabelStudioFiles::Error: Invalid entity_id: " + data['entity_id']
            
            
            current_app.logger.info(f"{self.__class__.__name__} :: path: {path}")

            xlsx_files = os.listdir(os.path.join(path, "xlsx"))

            if len(xlsx_files) > 0:
                FileUtility.signal_reformat_xlsx_v3(data['entity_id'], data['dataset_id'], data['subset_id'], self.file_set_id)


            FileUtility.move_files_to_local_storage_v2(data['entity_id'], data['dataset_id'], data['subset_id'])


            payload = { 
                "project": import_storage['ls_project_id'],
                "use_blob_urls": True
            }

            current_app.logger.info(f"{self.__class__.__name__} :: RequestSyncImportStorage payload: {payload}")
            api_request = RequestSyncImportStorage(import_storage['ls_import_id'], payload)
            response = api_request.do()
            current_app.logger.info(f"{self.__class__.__name__} :: RequestSyncImportStorage response: {response}")


            import_xlsx = HandleUploadGroundTruthLabelStudio()
            import_xlsx_response = import_xlsx.do_process(import_storage['ls_project_id'], data['entity_id'], data['dataset_id'], data['subset_id'])
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {import_xlsx_response}")

            return import_xlsx_response
            
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestSyncLabelStudioFiles -- do_process() Error: " + str(e)