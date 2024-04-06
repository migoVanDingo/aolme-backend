from api.files.AbstractFiles import AbstractFiles
class RequestArchiveFile(AbstractFiles):
    def __init__(self, data):
        self.data = data

    def do_process(self):
        return self.archive_file(self.data['file_id'])
    
    