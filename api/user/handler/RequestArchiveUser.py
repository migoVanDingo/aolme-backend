from api.user.AbstractUser import AbstractUser
class RequestArchiveUser(AbstractUser):
    def __init__(self, user_id):
        self.user_id = user_id

    def do_process(self):
        return self.archive_user(self.user_id)