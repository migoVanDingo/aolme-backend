from api.files import AbstractFiles
class RequestUpdateFile(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        return self.update_file(self.data['file_id'], self.data['file_name'], self.data['file_content'])