from datetime import datetime

from flask import current_app
from api.user.AbstractUser import AbstractUser
from dao.TableEntityUser import TableEntityUser

class RequestUpdateUser(AbstractUser):
    def __init__(self, user_id, params):
        super().__init__()
        self.user_id = user_id
        self.params = params

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: user_id: {self.user_id} :: payload: {self.params}")

            self.params["updated_at"] = "{}".format(datetime.now())
            updateEmail = self.update_user_email(self.params, self.user_id)
            current_app.logger.info(f"{self.__class__.__name__} :: updateEmail: {updateEmail}")

            updateUsername = self.update_username(self.params, self.user_id)
            current_app.logger.info(f"{self.__class__.__name__} :: updateUsername: {updateUsername}")


            entity_user_table = TableEntityUser()
            updateRoles = entity_user_table.update_entity_user_roles(self.params, self.params["entity_user_id"])
            current_app.logger.info(f"{self.__class__.__name__} :: updateRoles: {updateRoles}")


            updateStatus = entity_user_table.update_entity_user_status(self.params, self.params["entity_user_id"])
            current_app.logger.info(f"{self.__class__.__name__} :: updateStatus: {updateStatus}")

            

            response = {
                "status": "success",
                "message": "User updated: {}".format(self.user_id),
                "user_id": self.user_id
            }

            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")

            return response
    
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestUpdateUser -- do_process() Error: " + str(e)



