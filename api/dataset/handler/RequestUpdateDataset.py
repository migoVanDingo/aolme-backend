from api.dataset.AbstractDataset import AbstractDataset
class RequestUpdateDataset(AbstractDataset):
    def __init__(self, dataset_id, payload):
        self.dataset_id = dataset_id
        self.payload = payload

    def do_process(self):
        return self.update(self.dataset_id, self.payload)