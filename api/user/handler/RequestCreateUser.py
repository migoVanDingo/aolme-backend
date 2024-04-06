from datetime import datetime
import json

import requests
from api.directory_tree.handler.RequestCreateUserDirectory import RequestCreateUserDirectory
from api.user.AbstractUser import AbstractUser
from api.user.utility.CreateUserValidator import CreateUserValidator
from dao.TableEntityUser import TableEntityUser
class RequestCreateUser(AbstractUser):
    def __init__(self, params, entity_id=None, entity_type=None):
        super().__init__()
        self.params = params
        self.entity_id = entity_id
        self.entity_type = entity_type


    def do_process(self):
        try:

            

            params = {
                "username": self.params["username"],
                "email": self.params["email"],
                "hash": self.hash_password(self.params["password"]).decode('utf8') if "password" in self.params else self.hash_password("password").decode('utf8'), 
                "firstname": self.params["firstname"] if "firstname" in self.params else "",
                "lastname": self.params["lastname"] if "lastname" in self.params else "",
                "is_active": 1,
                "created_by": "root::MIGO" if "created_by" not in self.params else self.params["created_by"],
                "created_at": "{}".format(datetime.now()),
             
                

            }



            #Validate the payload sent from FE
            validator = CreateUserValidator()
            is_valid = validator.validate(params)
            if is_valid[0] is False:
                print("\nRequestCreateUser::do_process:: ERROR: {}\n\n".format(is_valid[1]))
                return is_valid[1]
            
            response = self.insert_user(params)
            del response['hash']

            if(self.entity_id is not None and self.entity_type is not None):
                entity_user = {
                    "entity_id": self.entity_id,
                    "entity_type": self.entity_type,
                    "entity_status": "ACTIVE",
                    "is_active": 1,
                    "roles": self.params["roles"] if "roles" in self.params else "USER",
                    "user_id": response['user_id'],
                    "user_status": "INVITED",
                    "created_by": "root::MIGO" if "created_by" not in params else params["created_by"],
                    "created_at": "{}".format(datetime.now())
                }
                entity_user_table = TableEntityUser()
                entity_user_response = entity_user_table.insert_entity_user(entity_user)
                print("\nENTITY_USER_RESPONSE: {}\n\n".format(entity_user_response))

            headers = {
                "Content-Type": "application/json"
            }

            print("CREATED_USER_ID: {}".format(response['user_id']))
            request_create_user_dirs = RequestCreateUserDirectory(response['user_id'])
            api_request = request_create_user_dirs.do_process()
            print("CREATE_USER_DIRECTORIES: {}".format(api_request))

            print("CREATE_USER_RESPONSE: {}".format(response))
            return response
        except Exception as e:
            print("RequestCreateUser::do_process:: ERROR: {}".format(str(e)))
            return "RequestCreateUser::do_process: ERROR: {}".format(str(e))

    