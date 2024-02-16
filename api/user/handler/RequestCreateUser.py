from datetime import datetime
import json

import requests
from api.user.AbstractUser import AbstractUser
from api.user.utility.CreateUserValidator import CreateUserValidator
class RequestCreateUser(AbstractUser):
    def __init__(self, params):
        super().__init__()
        self.params = params

    def do_process(self):

        print("PARAMS: {}".format(self.params))
        params = json.loads(self.params)
        print("PARAMS 2: {}".format(params["username"]))

        
        params = {
            "username": params["username"],
            "email": params["email"],
            "hash": self.hash_password(params["password"]).decode('utf8'), 
            "firstname": params["firstname"] if "firstname" in params else "",
            "lastname": params["lastname"] if "lastname" in params else "",
            "is_active": 1,
            "created_by": "root::MIGO",
            "created_at": datetime.now()
            

        }

        print("PARAMS 3: {}".format(params))

        #Validate the payload sent from FE
        validator = CreateUserValidator()
        is_valid = validator.validate(params)
        if is_valid[0] is False:
            return is_valid[1]
        
        response = self.insert_user(params)
        del response['hash']

        headers = {
            "Content-Type": "application/json"
        }

        self.url = "http://localhost:5000/api/directory/user/{}".format(response['user_id'])
        api_request = requests.post(self.url, headers=headers)
        print("CREATE_USER_DIRECTORIES: {}".format(api_request))

        print("CREATE_USER_RESPONSE: {}".format(response))
        return response

    