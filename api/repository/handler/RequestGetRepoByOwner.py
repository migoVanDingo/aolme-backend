from api.repository.AbstractRepository import AbstractRepository
class RequestGetRepoByOwner(AbstractRepository):
    def __init__(self, owner_id):
        super().__init__()
        self.owner_id = owner_id
        
    def do_process(self):
        return self.read_list_owner(self.owner_id)