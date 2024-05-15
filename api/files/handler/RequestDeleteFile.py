from flask import current_app
from api.files.AbstractFiles import AbstractFiles

class RequestDeleteFile(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: file_id: {self.data['file_id']}")
            response = self.delete_file(self.data['file_id'])
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404