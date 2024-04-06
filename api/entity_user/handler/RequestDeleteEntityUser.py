from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestDeleteEntityUser(AbstractEntityUser):
    def __init__(self, entity_user_id):
        super().__init__()
        self.entity_user_id = entity_user_id


    def do_process(self):
        return self.delete_entity_user(self.entity_user_id)