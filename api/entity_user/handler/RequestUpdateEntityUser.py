from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestUpdateEntityUser(AbstractEntityUser):
    def __init__(self, entity_user_id, user_id, entity_id, is_active):
        super().__init__()
        self.entity_user_id = entity_user_id
        self.user_id = user_id
        self.entity_id = entity_id
        self.is_active = is_active


    def do_process(self):
        return self.update_entity_user(self.entity_user_id, self.user_id, self.entity_id, self.is_active)