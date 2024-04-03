from flask import jsonify
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetSubsetItems(AbstractDataset):
    def __init__(self, subset_id):
        super().__init__()
        self.subset_id = subset_id

    def do_process(self):
        try:

            response = self.read_items_by_subset_id(self.subset_id)
            print("RequestGetSubsetItems -- do_process() response: " + str(response))
            return jsonify(response)
            
        except Exception as e:
            print("RequestGetSubsetItems -- do_process() Error: " + str(e))
            return "RequestGetSubsetItems -- do_process() Error: " + str(e)