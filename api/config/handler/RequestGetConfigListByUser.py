from api.config.AbstractConfig import AbstractConfig

class RequestGetConfigListByUser(AbstractConfig):
    def __init__(self, user_id):
        self.user_id = user_id

    def do_process(self):
        return self.read_list_by_user(self.user_id)