from api.user import AbstractUser

class RequestDeleteUser(AbstractUser):
    def __init__(self, user_id):
        self.user_id = user_id

    def do_process(self):
        return self.delete_user(self.user_id)