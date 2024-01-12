from api.user_group import AbstractUserGroup

class RequestUpdateUserGroup(AbstractUserGroup):
    def __init__(self, params):
        self.params = params

    def do_process(self):
        return self.update_user_group(self.params)