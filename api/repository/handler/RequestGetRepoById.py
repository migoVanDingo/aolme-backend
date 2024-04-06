from api.repository.AbstractRepository import AbstractRepository

class RequestGetRepoById(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id


    def do_process(self):
        return self.read(self.repo_id)