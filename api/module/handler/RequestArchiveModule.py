from api.module.AbstractModule import AbstractModule

class RequestArchiveModule(AbstractModule):
    def __init__(self, module_id):
        self.module_id = module_id

    def do_process(self):
        return self.archive(self.module_id)