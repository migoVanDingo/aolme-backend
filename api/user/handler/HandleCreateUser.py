import json
from dao.TableUser import TableUser

class HandleCreateUser:
    def __init__(self,data):
        self.data = data

    def do_process(self):

        table_user = TableUser()
        user = table_user.create_new_user(self.data)

        return user