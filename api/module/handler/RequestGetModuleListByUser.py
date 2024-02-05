from api.module.AbstractModule import AbstractModule
class RequestGetModuleListByUser(AbstractModule):
    def __init__(self, payload):
        self.payload = payload

    def do_process(self):
        return self.read_list_by_user(self.payload)