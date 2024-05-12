from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
class RequestDeleteDataset(AbstractDataset):
    def __init__(self, dataset_id):
        self.dataset_id = dataset_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: dataset_id: {self.dataset_id}")
            response = self.delete(self.dataset_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
    
    