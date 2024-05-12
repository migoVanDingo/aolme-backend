import json

from flask import current_app
from dao.TableUser import TableUser

class HandleGetUser:
    def __init__(self,user_id):
        self.user_id = user_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: user_id: {self.user_id}")
            table_user = TableUser()
            user = table_user.get_user_by_id(self.user_id)
            (user,) = user
            del user['hash']

            current_app.logger.info(f"{self.__class__.__name__} :: User: {user}")
        
            return user
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"
        