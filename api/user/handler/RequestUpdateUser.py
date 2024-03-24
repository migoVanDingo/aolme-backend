from datetime import datetime
from api.user.AbstractUser import AbstractUser
from dao.TableEntityUser import TableEntityUser

class RequestUpdateUser(AbstractUser):
    def __init__(self, user_id, params):
        super().__init__()
        self.user_id = user_id
        self.params = params

    def do_process(self):
        try:

            print("\n params: {}\n\n".format(self.params))

            print("\n userId: {}\n\n".format(self.user_id))
            self.params["updated_at"] = "{}".format(datetime.now())
            updateEmail = self.update_user_email(self.params, self.user_id)
            print("\n updateEmail: {}\n".format(updateEmail))
            updateUsername = self.update_username(self.params, self.user_id)
            print("\n updateUsername: {}\n".format(updateUsername))


            entity_user_table = TableEntityUser()
            updateRoles = entity_user_table.update_entity_user_roles(self.params, self.params["entity_user_id"])
            print("\n updateRoles: {}\n".format(updateRoles))


            updateStatus = entity_user_table.update_entity_user_status(self.params, self.params["entity_user_id"])

            print("\n updateStatus: {}\n".format(updateStatus)) 

            

            response = {
                "status": "success",
                "message": "User updated: {}".format(self.user_id),
                "user_id": self.user_id
            }

            return response
    
        except Exception as e:
            print("RequestUpdateUser -- do_process() Error: " + str(e))
            return "RequestUpdateUser -- do_process() Error: " + str(e)



