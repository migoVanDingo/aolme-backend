from datetime import datetime, timedelta
import json
from api.entity_user.utility.InsertEntityUserValidator import InsertEntityUserValidator
from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestInsertEntityUser(AbstractEntityUser):
    def __init__(self, params):
        super().__init__()
        self.params = params


    def do_process(self):

        self.params['is_active'] = True
        self.params['created_at'] = datetime.now()
        self.params['created_by'] = self.params['user_id']
        self.params['active_from'] = datetime.now() if 'active_from' not in self.params else self.params['active_from']
        self.params['active_to'] = datetime.now() + timedelta(days=50000) if 'active_to' not in self.params else self.params['active_to']


        print("type: {}".format(type(self.params['created_at'])))

        validator = InsertEntityUserValidator()
        is_valid = validator.validate(self.params)
        if is_valid[0] is False:
            return is_valid[1]
        
        self.params['roles'] = json.dumps(self.params['roles'])

        return self.create_entity_user(self.params)