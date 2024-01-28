from api.repository.AbstractRepository import AbstractRepository
class RequestGetRepoByEntity(AbstractRepository):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id
        


    def do_process(self):
        return self.read_list_entity(self.entity_id)
    