from api.dataset.AbstractDataset import AbstractDataset
class RequestGetSubset(AbstractDataset):
    def __init__(self,subset_id):
        super().__init__()
        self.subset_id = subset_id
        
    def do_process(self):
        try:

            response = self.read_subset(self.subset_id)
            return response
            
        except Exception as e:
            print("RequestGetSubset -- do_process() Error: " + str(e))
            return "RequestGetSubset -- do_process() Error: " + str(e)