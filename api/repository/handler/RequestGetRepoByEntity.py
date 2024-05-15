from flask import current_app
from api.repository.AbstractRepository import AbstractRepository
class RequestGetRepoByEntity(AbstractRepository):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id
        


    def do_process(self):
        try:  
            current_app.logger.debug(f"{self.__class__.__name__} :: entity_id: {self.entity_id}")  
            response = self.read_list_entity(self.entity_id)

            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
    
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"
