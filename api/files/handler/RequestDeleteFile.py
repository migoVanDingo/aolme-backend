from api.files.AbstractFiles import AbstractFiles

class RequestDeleteFile(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        return self.delete_file(self.data['file_id'])