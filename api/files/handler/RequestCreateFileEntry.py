from api.files import AbstractFiles

class RequestCreateFileEntry(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        return self.insert_file(self.data['file_name'], self.data['file_content'])