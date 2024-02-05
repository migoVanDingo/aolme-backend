from datetime import datetime, timedelta
import json
from api.entity_user.utility.InsertEntityUserValidator import InsertEntityUserValidator
from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestInsertEntityUser(AbstractEntityUser):
    def __init__(self, params):
        super().__init__()
        self.params = params


    def do_process(self):
        print('here')
        self.params['is_active'] = True
        self.params['created_at'] = "{}".format(datetime.now())
        self.params['created_by'] = self.params['user_id']
        


        print("SELF_PARAMS: {}".format(self.params['created_at']))

        validator = InsertEntityUserValidator()
        is_valid = validator.validate(self.params)
        if is_valid[0] is False:
            return is_valid[1]
        
       #self.params['roles'] = json.dumps(self.params['roles'])

        
        response =  self.create_entity_user(self.params)

        print("REQUEST_INSERT_ENTITY_USER_RESPONSE: {}".format(response))

        return response