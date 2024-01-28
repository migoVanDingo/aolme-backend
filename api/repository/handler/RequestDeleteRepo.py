from api.repository.AbstractRepository import AbstractRepository
class RequestDeleteRepo(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id


    def do_process(self):
        return self.delete(self.repo_id)