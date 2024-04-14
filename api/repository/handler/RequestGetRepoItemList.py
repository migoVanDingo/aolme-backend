from flask import jsonify
from api.repository.AbstractRepository import AbstractRepository

class RequestGetRepoItemList(AbstractRepository):
    def __init__(self, repo_id):
        super().__init__()
        self.repo_id = repo_id

    def do_process(self):
        try:
            response = jsonify(self.read_list_repo_items(self.repo_id))

            return response
        
        except Exception as e:
            print("RequestGetRepoItemList -- do_process() Error: " + str(e))
            return "RequestGetRepoItemList -- do_process() Error: " + str(e)