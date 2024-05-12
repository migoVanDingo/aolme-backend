from flask import current_app
from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestArchiveEntityUser(AbstractEntityUser):
    def __init__(self, entity_user_id):
        super().__init__()
        self.entity_user_id = entity_user_id


    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: entity_user_id: {self.entity_user_id}")
            response = self.archive_entity_user(self.entity_user_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404