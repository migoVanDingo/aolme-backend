from flask import current_app
from api.repository.AbstractRepository import AbstractRepository
class RequestGetRepoByOwner(AbstractRepository):
    def __init__(self, owner_id):
        super().__init__()
        self.owner_id = owner_id
        
    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: owner_id: {self.owner_id}")
            response = self.read_list_owner(self.owner_id)

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"