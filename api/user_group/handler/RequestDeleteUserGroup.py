from api.user_group import AbstractUserGroup

class RequestDeleteUserGroup(AbstractUserGroup):
    def __init__(self, user_group_id):
        self.user_group_id = user_group_id

    def do_process(self):
        return self.delete_user_group(self.user_group_id)