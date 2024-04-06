from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestGetEntityListByUserId(AbstractEntityUser):
    def __init__(self, user_id):
        super().__init__()
        self.user_id = user_id


    def do_process(self):
        return self.get_entity_list_by_user_id(self.user_id)