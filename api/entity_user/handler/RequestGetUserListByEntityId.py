from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestGetUserListByEntityId(AbstractEntityUser):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id


    def do_process(self):
        return self.get_user_list_by_entity_id(self.entity_id)