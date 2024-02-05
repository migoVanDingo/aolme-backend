from api.dataset.AbstractDataset import AbstractDataset

class RequestGetDatasetListByEntity(AbstractDataset):
    def __init__(self, entity_id):
        self.entity_id = entity_id

    def do_process(self):
        return self.read_list_by_entity(self.entity_id)