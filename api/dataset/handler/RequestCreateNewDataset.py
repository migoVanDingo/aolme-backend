from api.dataset.AbstractDataset import AbstractDataset

class RequestCreateDataset(AbstractDataset):
    def __init__(self, payload):
        self.payload = payload

    def do_process(self):
        return self.create(self.payload)