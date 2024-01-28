from api.repository.AbstractRepository import AbstractRepository
from datetime import datetime
class RequestCreateRepository(AbstractRepository):
    def __init__(self, payload):
        super().__init__()
        self.payload = payload


    def do_process(self):

        self.payload["created_at"] = datetime.now()
        self.payload["is_active"] = True


        return self.create(self.payload)