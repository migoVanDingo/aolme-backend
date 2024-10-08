from flask import current_app, jsonify
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetDatasetListByEntity(AbstractDataset):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: entity_id: {self.entity_id}")
            response =  self.read_list_by_entity(self.entity_id)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return jsonify(response)
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetDatasetListByEntity -- do_process() Error: " + str(e)
