from flask import current_app, jsonify
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetSubsetList(AbstractDataset):
    def __init__(self, dataset_id):
        super().__init__()
        self.dataset_id = dataset_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: dataset_id: {self.dataset_id}")
            response =  self.read_list_by_dataset_id(self.dataset_id)

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return jsonify(response)
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetSubsetList -- do_process() Error: " + str(e)