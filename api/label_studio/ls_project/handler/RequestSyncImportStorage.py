from flask import current_app, jsonify
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestSyncImportStorage(AbstractLsProject):
    def __init__(self, storage_id, payload):
        super().__init__()
        self.storage_id = storage_id
        self.payload = payload

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")

            response = self.sync_import_storage(self.storage_id, self.payload)

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404

