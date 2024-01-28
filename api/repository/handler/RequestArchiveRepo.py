from api.repository.AbstractRepository import AbstractRepository

class RequestArchiveRepo(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id


    def do_process(self):
        return self.archive(self.repo_id)