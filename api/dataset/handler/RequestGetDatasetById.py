from flask import jsonify
from api.dataset.AbstractDataset import AbstractDataset


class RequestGetDatasetById(AbstractDataset):
    def __init__(self, dataset_id):
        super().__init__()
        self.dataset_id = dataset_id

    def do_process(self):
        try:
            response = self.read_item(self.dataset_id)
            return jsonify(response)
        except Exception as e:
            print("RequestGetDatasetById -- do_process() Error: " + str(e))
            return "RequestGetDatasetById -- do_process() Error: " + str(e)
