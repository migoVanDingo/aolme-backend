from dao.TableUser import TableUser


class HandleLogin:
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            table_user = TableUser()
            user = table_user.get_user_by_username(self.data['username'])
            
            print("data: {}".format(self.data))
            

            (user) = user
            print("user: {}".format(user))

            

            if self.data['password'] == user['hash']:
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