import datetime
from api.user_group.AbstractUserGroup import AbstractUserGroup
from api.user_group.utility.CreateUserGroupValidator import CreateUserGroupValidator

class RequestCreateUserGroup(AbstractUserGroup):
    def __init__(self, params):
        self.params = params

    def do_process(self):

        self.params['created_at'] = datetime.now()

        validator = CreateUserGroupValidator(self.params)
        is_valid = validator.validate()
        if is_valid[0] is False:
            return "Error: INVALID_PAYLOAD :: RequestCreateUserGroup -- do_process() -- " + is_valid[1]
        

        return self.insert_user_group(self.data['user_group_name'])