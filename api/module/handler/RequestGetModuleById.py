from api.module.AbstractModule import AbstractModule

class RequestGetModuleById(AbstractModule):
    def __init__(self, module_id):
        self.module_id = module_id

    def do_process(self):
        return self.read_item(self.module_id)