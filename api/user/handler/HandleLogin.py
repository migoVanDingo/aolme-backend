from flask import current_app
from dao.TableUser import TableUser
from api.user.AbstractUser import AbstractUser


class HandleLogin(AbstractUser):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: Login User :: payload: {self.data}")
            table_user = TableUser()
            user = table_user.get_user_by_email(self.data['email'])


            current_app.logger.info(f"{self.__class__.__name__} :: User: {user}")
            

            (user) = user
        

            if self.check_password(self.data['password'], user['hash']):
                response = {
                    "userId": user['user_id'],
                    "email": user['email'],
                    "username": user['username']
                }
                current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")

                return response
            else:
                current_app.logger.error(f"{self.__class__.__name__} :: Response: ERROR: Passwords don't match")
                return "ERROR: Passwords don't match"

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}" 