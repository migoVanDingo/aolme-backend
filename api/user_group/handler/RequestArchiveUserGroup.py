from flask import current_app
from api.user_group.AbstractUserGroup import AbstractUserGroup

class RequestArchiveUserGroup(AbstractUserGroup):
    def __init__(self, user_group_id):
        self.user_group_id = user_group_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: user_group_id: {self.user_group_id}")
            response = self.archive_user_group(self.user_group_id)
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404