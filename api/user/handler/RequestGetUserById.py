from api.user import AbstractUser
class RequestGetUserById(AbstractUser):
    def __init__(self, user_id):
        self.user_id = user_id

    def do_process(self):
        return self.get_user_by_id(self.user_id)