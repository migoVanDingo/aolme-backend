import datetime
from api.user.AbstractUser import AbstractUser

class RequestUpdateUser(AbstractUser):
    def __init__(self, user_id, params):
        self.user_id = user_id
        self.params = params

    def do_process(self):

        params = {
            "user_id": self.user_id,
            "username": self.params['username'],
            "email": self.params['email'],
            "hash": self.params['hash'],
            "firstname": self.params['firstname'] if 'firstname' in self.params else "",
            "lastname": self.params['lastname'] if 'lastname' in self.params else "",
            "updated_by": self.params['updated_by'],
            "updated_at": datetime.now(),
        }

        return self.update_user(params)