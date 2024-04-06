from api.file_upload.FileUtility import FileUtility


class RequestGroundTruthConversions:
    def __init__(self, data):
        self.data = data

    def do_process(self):
        print("RequestGroundTruthConversions::do_process::data: {}".format(self.data))
        return FileUtility.signal_reformat_xlsx_v2(self.data)
    