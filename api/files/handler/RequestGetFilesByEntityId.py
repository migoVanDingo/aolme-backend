from api.files.AbstractFiles import AbstractFiles

class RequestGetFilesByEntityId(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        return self.read_file(self.data['entity_id'])
    