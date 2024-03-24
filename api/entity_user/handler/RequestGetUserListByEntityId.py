from api.entity_user.AbstractEntityUser import AbstractEntityUser

class RequestGetUserListByEntityId(AbstractEntityUser):
    def __init__(self, entity_id):
        super().__init__()
        self.entity_id = entity_id


    def do_process(self):
        try:
            print("GET_USER_LIST_BY_ENTITY_ID: {}".format(self.entity_id))
            response = self.get_user_list_by_entity_id(self.entity_id)

            print("GET_USER_LIST_BY_ENTITY_ID_RESPONSE: {}".format(response))   

            return response
        
        except Exception as e:
            print("RequestGetUserListByEntityId::::do_process():::: Error: {}".format(str(e)))
            return e, 404