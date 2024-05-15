from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
class RequestGetDatasetList(AbstractDataset):
    def __init__(self):
        pass

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: RequestGetDatasetList")
            response = self.read_list()
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        