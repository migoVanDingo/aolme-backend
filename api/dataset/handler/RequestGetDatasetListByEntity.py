from flask import jsonify
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetDatasetListByEntity(AbstractDataset):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id

    def do_process(self):
        try:

            response =  self.read_list_by_entity(self.entity_id)
            print("RequestGetDatasetListByEntity -- do_process() response: " + str(response))
            return jsonify(response)
        
        except Exception as e:
            print("RequestGetDatasetListByEntity -- do_process() Error: " + str(e))
            return "RequestGetDatasetListByEntity -- do_process() Error: " + str(e)
