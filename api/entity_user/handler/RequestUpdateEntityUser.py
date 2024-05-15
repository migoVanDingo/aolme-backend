from flask import current_app
from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestUpdateEntityUser(AbstractEntityUser):
    def __init__(self, entity_user_id, user_id, entity_id, is_active):
        super().__init__()
        self.entity_user_id = entity_user_id
        self.user_id = user_id
        self.entity_id = entity_id
        self.is_active = is_active


    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: entity_user_id: {self.entity_user_id}, user_id: {self.user_id}, entity_id: {self.entity_id}, is_active: {self.is_active}")
            response = self.update_entity_user(self.entity_user_id, self.user_id, self.entity_id, self.is_active)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404