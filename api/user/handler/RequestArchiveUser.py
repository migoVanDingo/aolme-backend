from flask import current_app
from api.user.AbstractUser import AbstractUser
class RequestArchiveUser(AbstractUser):
    def __init__(self, user_id):
        self.user_id = user_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: user_id: {self.user_id}")
            return self.archive_user(self.user_id)
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}"