import json
from dao.TableUser import TableUser

class HandleGetUser:
    def __init__(self,user_id):
        self.user_id = user_id

    def do_process(self):

        table_user = TableUser()
        user = table_user.get_user_by_id(self.user_id)
        (user,) = user
        del user['hash']

        return user