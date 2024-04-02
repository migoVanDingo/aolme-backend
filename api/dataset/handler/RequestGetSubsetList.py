from flask import jsonify
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetSubsetList(AbstractDataset):
    def __init__(self, dataset_id):
        super().__init__()
        self.dataset_id = dataset_id

    def do_process(self):
        try:

            response =  self.read_list_by_dataset_id(self.dataset_id)
            return jsonify(response)
        
        except Exception as e:
            print("RequestGetSubsetList -- do_process() Error: " + str(e))
            return "RequestGetSubsetList -- do_process() Error: " + str(e)