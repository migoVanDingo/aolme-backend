import datetime

from flask import current_app
from api.user_group.AbstractUserGroup import AbstractUserGroup
from api.user_group.utility.CreateUserGroupValidator import CreateUserGroupValidator

class RequestCreateUserGroup(AbstractUserGroup):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: params: {self.params}")
            self.params['created_at'] = datetime.now()

            validator = CreateUserGroupValidator(self.params)
            is_valid = validator.validate()
            if is_valid[0] is False:
                current_app.logger.error(f"{self.__class__.__name__} :: Error: INVALID_PAYLOAD -- {is_valid[1]}")
                return "Error: INVALID_PAYLOAD :: RequestCreateUserGroup -- do_process() -- " + is_valid[1]
            

            response = self.insert_user_group(self.data['user_group_name'])
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404