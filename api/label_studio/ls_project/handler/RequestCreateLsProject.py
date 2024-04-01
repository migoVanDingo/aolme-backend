from datetime import datetime
import json
import os

from flask import jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject
from dao.TableLsImportStorage import TableLsImportStorage


class RequestCreateLsProject(AbstractLsProject):
    def __init__(self):
        super().__init__()

    def do_process(self, payload):
        try:

            # Create the ls project Payload
            payload_create_project = {
                "title": payload['name'], "description": payload['description']}

            print("Payload: {}".format(json.dumps(payload_create_project)))

            # Create the ls project
            response = self.create_ls_project(
                json.dumps(payload_create_project))

            print("Created ls project: {}".format(response))

            payload_persist_ls_project = {
                "name": payload['name'],
                "description": payload['description'],
                "ls_project_id": response['id'],
                "entity_id": payload['owner'],
                "repo_id": payload['repo_id'],
                "is_active": True,
                "created_by": payload['created_by'],
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }

            persist_ls_project = self.insert_ls_project(
                payload_persist_ls_project)

            print("Persisted ls project: {}".format(persist_ls_project))

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

            # Create the webhook to get updated files
            create_webhook = self.create_webhook(payload_create_webhook)

            print("Created webhook: {}".format(create_webhook))

            # Create import storage payload
            # path = os.path.join(
            #     os.environ["USER_DIRECTORY"], payload['created_by'])
            # path = os.path.join(path, "repo")
            # path = os.path.join(path, payload['repo_id'])
            # path = os.path.join(path, "files")
            # path = os.path.join(path, "uploads")

            import_storage_path = os.path.join(
                os.environ["REPO_DIRECTORY"], payload['repo_id'])
            import_storage_path = os.path.join(import_storage_path, "local-storage")

            print("Import storage path: {}".format(import_storage_path))
            #test_path = "/Users/bubz/Developer/master-project/aolme-backend/project/334/videos"

            #print("Test path: {}".format(test_path))
            
            payload_create_import_storage = {
                "project": int(response['id']),
                "title": payload['name'],
                "description": payload['description'],
                "path": import_storage_path,
                "use_blob_urls": True,
            }

            print("payload_create_import_storage: {}".format(payload_create_import_storage))

            # Create the import storage
            create_import_storage = self.create_import_storage(
                json.dumps(payload_create_import_storage)).json()

            print("Created import storage: {}".format(create_import_storage))

            payload_sync_import_storage = {
                "project": payload_create_import_storage['project'],
                "use_blob_urls": True
            }

            


            


            sync_import_storage = self.sync_import_storage(
                create_import_storage['id'], payload_sync_import_storage)
            
            dao_insert_import_storage = {
                "ls_id": create_import_storage['id'],
                "entity_id": payload_persist_ls_project['entity_id'],
                "repo_id": payload['repo_id'],
                "title": payload['name'],
                "path": import_storage_path,
                "created_by": payload['created_by'],
                "project_id": payload_create_import_storage['project'],
                "user_id": payload['created_by']
            }

            print("RequestCreateLsProject::dao_insert_import_storage payload: {}".format(dao_insert_import_storage))

            dao_import_storage = TableLsImportStorage()
            insert_import_storage = dao_import_storage.insert_ls_import_storage(dao_insert_import_storage)

            print("RequestCreateLsProject::Inserted import storage: {}".format(insert_import_storage))
            
            print("Synced import storage: {}".format(sync_import_storage.json()))

            return response

        except Exception as e:
            print("RequestCreateLsProject::::do_process():::: Error: {}".format(str(e)))
            return "RequestCreateLsProject::::do_process():::: Error:" + str(e), 404


""" 
      

             

            #Create the sync import storage payload
            payload_sync_import_storage = {
                "project": response['id'],
                "use_blob_urls": True
            }

            #Sync the import storage
            #sync_import_storage = self.sync_import_storage(create_import_storage['id'], payload_sync_import_storage)

            #print("Synced import storage: {}".format(sync_import_storage))       
 """
