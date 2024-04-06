from api.config.AbstractConfig import AbstractConfig

class RequestGetConfigListPublic(AbstractConfig):
    def __init__(self):
        pass

    def do_process(self):
        return self.read_list()