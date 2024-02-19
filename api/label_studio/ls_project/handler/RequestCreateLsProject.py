from datetime import datetime
import json
import os

from flask import jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject


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
            path = os.path.join(
                os.environ["USER_DIRECTORY"], payload['created_by'])
            path = os.path.join(path, "project")
            
            payload_create_import_storage = {
                "project": int(response['id']),
                "title": payload['name'],
                "description": payload['description'],
                "path": path,
                "use_blob_urls": True,
            }

            print("payload_create_import_storage: {}".format(payload_create_import_storage))

            # Create the import storage
            create_import_storage = self.create_import_storage(
                json.dumps(payload_create_import_storage))

            print("Created import storage: {}".format(create_import_storage))

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
