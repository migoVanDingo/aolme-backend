from datetime import datetime, timedelta
import json

from flask import current_app
from api.entity_user.utility.InsertEntityUserValidator import InsertEntityUserValidator
from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestInsertEntityUser(AbstractEntityUser):
    def __init__(self, params):
        super().__init__()
        self.params = params


    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.params}")

            self.params['is_active'] = True
            self.params['created_at'] = "{}".format(datetime.now())
            self.params['created_by'] = self.params['user_id']
            

            validator = InsertEntityUserValidator()
            is_valid = validator.validate(self.params)
            if is_valid[0] is False:
                current_app.logger.error(f"{self.__class__.__name__} :: ERROR: Invalid Payload: {is_valid[1]}")
                return is_valid[1]
            
        #self.params['roles'] = json.dumps(self.params['roles'])
            current_app.logger.debug(f"{self.__class__.__name__} :: create-entity-user-payload: {self.params}")

            
            response =  self.create_entity_user(self.params)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")

        

            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
