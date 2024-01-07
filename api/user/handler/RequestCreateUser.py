import datetime
from api.user import AbstractUser
from api.user.utility.CreateUserValidator import CreateUserValidator
class RequestCreateUser(AbstractUser):
    def __init__(self, params):
        self.params = params

    def do_process(self):

        params = {
            "username": self.params['username'],
            "email": self.params['email'],
            "hash": self.params['hash'], 
            "firstname": self.params['firstname'] if 'firstname' in self.params else "",
            "lastname": self.params['lastname'] if 'lastname' in self.params else "",
            "is_active": True,
            "created_by": self.params['created_by'],
            "created_at": datetime.now(),
            

        }

        #Validate the payload sent from FE
        validator = CreateUserValidator()
        is_valid = validator.validate(params)
        if is_valid[0] is False:
            return is_valid[1]
        

        return self.create_user(params)

    