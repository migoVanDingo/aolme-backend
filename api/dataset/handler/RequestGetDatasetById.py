from api.dataset.AbstractDataset import AbstractDataset
class RequestGetDatasetById(AbstractDataset):
    def __init__(self, dataset_id):
        self.dataset_id = dataset_id

    def do_process(self):
        return self.read_item(self.dataset_id)