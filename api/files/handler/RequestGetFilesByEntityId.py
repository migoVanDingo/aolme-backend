from flask import current_app
from api.files.AbstractFiles import AbstractFiles

class RequestGetFilesByEntityId(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: entity_id: {self.data['entity_id']}")
            
            response = self.read_file(self.data['entity_id'])
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404