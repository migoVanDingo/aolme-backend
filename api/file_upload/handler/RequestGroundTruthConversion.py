from flask import current_app
from api.file_upload.FileUtility import FileUtility


class RequestGroundTruthConversions:
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.data}")
        
            response = FileUtility.signal_reformat_xlsx_v2(self.data)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
    