from flask import current_app
from api.files.AbstractFiles import AbstractFiles
class RequestUpdateFile(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.data}")
            response = self.update_file_info(self.data['file_id'], self.data['file_name'], self.data['file_content'])
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404