from api.repository.AbstractRepository import AbstractRepository

class RequestAddRepoItem(AbstractRepository):
    def __init__(self, repo_id, data):
        super().__init__()
        self.repo_id = repo_id
        self.data = data

    def do_process(self):
        try:
            payload = {
                "file_id": self.data['file_id'],
                "repo_id": self.repo_id,
                "type": self.data['file_type'],
                "user_id": self.data['user_id'],
            }
            response = self.add_repo_item(payload)
            return response
        except Exception as e:
            print("RequestAddRepoItem -- do_process() Error: " + str(e))
            return "RequestAddRepoItem -- do_process() Error: " + str(e)