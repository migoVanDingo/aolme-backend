import json

from flask import current_app
from dao.TableUser import TableUser

class HandleCreateUser:
    def __init__(self,data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data}")
            
            table_user = TableUser()
            user = table_user.create_new_user(self.data)

            current_app.logger.info(f"{self.__class__.__name__} :: User: {user}")
            return user
    
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"