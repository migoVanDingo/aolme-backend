from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
class RequestGetSubset(AbstractDataset):
    def __init__(self,subset_id):
        super().__init__()
        self.subset_id = subset_id
        
    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: subset_id: {self.subset_id}")
            response = self.read_subset(self.subset_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
            
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetSubset -- do_process() Error: " + str(e)