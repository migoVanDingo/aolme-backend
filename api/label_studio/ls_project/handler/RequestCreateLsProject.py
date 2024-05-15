from datetime import datetime
import json
import os

from flask import current_app, jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject
from dao.TableDatasetV2 import TableDatasetV2
from dao.TableLsImportStorage import TableLsImportStorage


class RequestCreateLsProject(AbstractLsProject):
    def __init__(self):
        super().__init__()

    def do_process(self, payload):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {payload}")
            table_dataset = TableDatasetV2()
            dataset = table_dataset.read_item(payload['dataset_id'])

            current_app.logger.debug(f"{self.__class__.__name__} :: dataset: {dataset}")
            
            if dataset['entity_id'].startswith("ORG"):
                subset_path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], dataset['entity_id'], "dataset", payload["dataset_id"], "subset", payload["subset_id"])
            elif dataset['entity_id'].startswith("USR"):
                subset_path = os.path.join(os.environ["USER_DIRECTORY"], dataset['entity_id'], "dataset", payload["dataset_id"], "subset", payload["subset_id"])    

            current_app.logger.debug(f"{self.__class__.__name__} :: subset_path: {subset_path}")
            # Create the ls project Payload
            payload_create_project = {
                "title": payload['name'], "description": payload['description']}

 
            current_app.logger.debug(f"{self.__class__.__name__} :: payload_create_project: {payload_create_project}")

            # Create the ls project
            response = self.create_ls_project(
                json.dumps(payload_create_project))
            
            current_app.logger.debug(f"{self.__class__.__name__} :: create-project-response: {response}")

            payload_persist_ls_project = {
                "name": payload['name'],
                "description": payload['description'],
                "ls_project_id": response['id'],
                "entity_id": payload['owner'],
                "subset_id": payload['subset_id'],
                "is_active": True,
                "created_by": payload['created_by'],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            current_app.logger.debug(f"{self.__class__.__name__} :: payload_persist_ls_project: {payload_persist_ls_project}")

            persist_ls_project = self.insert_ls_project(
                payload_persist_ls_project)

   
            current_app.logger.debug(f"{self.__class__.__name__} :: persist_ls_project: {persist_ls_project}")

            # initialize the webhook
            payload_create_webhook = {
                "actions": [
                    "PROJECT_UPDATED"
                ],
                "headers": {},
                "is_active": True,
                "project": int(response['id']),
                "send_for_all_actions": True,
                "send_payload": True,
                "url": "http://127.0.0.1:5000/api/webhook-handler/project-created"
            }

            current_app.logger.debug(f"{self.__class__.__name__} :: payload_create_webhook: {payload_create_webhook}")

            # Create the webhook to get updated files
            create_webhook = self.create_webhook(payload_create_webhook)

            current_app.logger.debug(f"{self.__class__.__name__} :: create_webhook: {create_webhook}")

            # Create import storage payload
            # path = os.path.join(
            #     os.environ["USER_DIRECTORY"], payload['created_by'])
            # path = os.path.join(path, "repo")
            # path = os.path.join(path, payload['subset_id'])
            # path = os.path.join(path, "files")
            # path = os.path.join(path, "uploads")

            # import_storage_path = os.path.join(
            #     os.environ["REPO_DIRECTORY"], payload['subset_id'])
            import_storage_path = os.path.join(subset_path, "local-storage")
        
            current_app.logger.debug(f"{self.__class__.__name__} :: import_storage_path: {import_storage_path}")

            
            payload_create_import_storage = {
                "project": int(response['id']),
                "title": payload['name'],
                "description": payload['description'],
                "path": import_storage_path,
                "use_blob_urls": True,
                "ls_import_id": persist_ls_project['ls_project_id']
            }

            current_app.logger.debug(f"{self.__class__.__name__} :: payload_create_import_storage: {payload_create_import_storage}")


            # Create the import storage
            create_import_storage = self.create_import_storage(
                json.dumps(payload_create_import_storage)).json()


            current_app.logger.debug(f"{self.__class__.__name__} :: create_import_storage: {create_import_storage}") 

            payload_sync_import_storage = {
                "project": payload_create_import_storage['project'],
                "use_blob_urls": True
            }

            current_app.logger.debug(f"{self.__class__.__name__} :: payload_sync_import_storage: {payload_sync_import_storage}")

            sync_import_storage = self.sync_import_storage(
                create_import_storage['id'], payload_sync_import_storage)
            
            current_app.logger.debug(f"{self.__class__.__name__} :: sync_import_storage: {sync_import_storage}")
            
            dao_insert_import_storage = {
                "ls_import_id": create_import_storage['id'],
                "entity_id": payload_persist_ls_project['entity_id'],
                "subset_id": payload['subset_id'],
                "title": payload['name'],
                "path": import_storage_path,
                "created_by": payload['created_by'],
                "ls_project_id": payload_create_import_storage['project'],
                "user_id": payload['created_by']
            }
            current_app.logger.debug(f"{self.__class__.__name__} :: dao_insert_import_storage: {dao_insert_import_storage}")


            dao_import_storage = TableLsImportStorage()
            insert_import_storage = dao_import_storage.insert_ls_import_storage(dao_insert_import_storage)

            current_app.logger.debug(f"{self.__class__.__name__} :: insert_import_storage: {insert_import_storage}")

                
            current_app.logger.debug(f"{self.__class__.__name__} :: sync_import_storage: {sync_import_storage.json()}")
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")   

            return response

        except Exception as e:
            current_app.logger.error(
                f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestCreateLsProject::::do_process():::: Error:" + str(e), 404

