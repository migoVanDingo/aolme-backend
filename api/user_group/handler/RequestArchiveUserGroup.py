from api.user_group.AbstractUserGroup import AbstractUserGroup

class RequestArchiveUserGroup(AbstractUserGroup):
    def __init__(self, user_group_id):
        self.user_group_id = user_group_id

    def do_process(self):
        return self.archive_user_group(self.user_group_id)