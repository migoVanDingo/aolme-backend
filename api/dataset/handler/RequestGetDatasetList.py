from api.dataset.AbstractDataset import AbstractDataset
class RequestGetDatasetList(AbstractDataset):
    def __init__(self):
        pass

    def do_process(self):
        return self.read_list()