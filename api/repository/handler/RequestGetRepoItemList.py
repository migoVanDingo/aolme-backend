from api.repository.AbstractRepository import AbstractRepository

class RequestGetRepoItemList(AbstractRepository):
    def __init__(self, repo_id):
        self.repo_id = repo_id

    def do_process(self):
        return self.read_list_repo_items(self.repo_id)