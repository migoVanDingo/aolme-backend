from dao.TableUser import TableUser
from api.user.AbstractUser import AbstractUser


class HandleLogin(AbstractUser):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            table_user = TableUser()
            user = table_user.get_user_by_email(self.data['email'])
            
            print("data: {}".format(self.data))
            

            (user) = user
            print("user: {}".format(user))

            
            print("decoded PW: {}".format(user['hash']))
            print("pws  {}".format(self.check_password(self.data['password'], user['hash'])))

            if self.check_password(self.data['password'], user['hash']):
                response = {
                    "userId": user['user_id'],
                    "email": user['email'],
                    "username": user['username']
                }

                return response
            else:
                return "ERROR: Passwords don't match"

        except Exception as e:
            return "TableUser -- get_user_by_username() Error: " + str(e) 