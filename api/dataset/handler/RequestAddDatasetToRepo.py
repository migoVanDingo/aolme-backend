from api.dataset.AbstractDataset import AbstractDataset

class RequestAddDatasetToRepo(AbstractDataset):
    def __init__(self, params, files):
        super().__init__()
        self.params = params
        self.files = files

    def do_process(self):
        try:
            
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404
        
    