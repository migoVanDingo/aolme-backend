from flask import current_app
from api.user_group.AbstractUserGroup import AbstractUserGroup

class RequestUpdateUserGroup(AbstractUserGroup):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.params}")
            
            response = self.update_user_group(self.params)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")

            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404