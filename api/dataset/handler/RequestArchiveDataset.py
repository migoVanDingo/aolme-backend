from api.dataset.AbstractDataset import AbstractDataset

class RequestArchiveDataset(AbstractDataset):
    def __init__(self, dataset_id):
        self.dataset_id = dataset_id

    def do_process(self):
        return self.archive(self.dataset_id)