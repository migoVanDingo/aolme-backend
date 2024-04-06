from api.repository.AbstractRepository import AbstractRepository

class RequestUpdateRepo(AbstractRepository):
    def __init__(self, repo_id, payload):
        super().__init__()
        self.repo_id = repo_id
        self.payload = payload


    def do_process(self):
        return self.update(self.repo_id, self.payload)