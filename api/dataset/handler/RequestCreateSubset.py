import os
from api.dataset.AbstractDataset import AbstractDataset
from dao.TableDatasetV2 import TableDatasetV2
class RequestCreateSubset(AbstractDataset):
    def __init__(self,data,files):
        super().__init__()
        self.data = data
        self.files = files
        
    def do_process(self):
        try:
            dataset = TableDatasetV2()
            dataset_data = dataset.read_item(self.data['dataset_id'])


            path = ""
            if(dataset_data['entity_id'].startswith("ORG")):
                path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], dataset_data['entity_id'], "dataset")
            elif(dataset_data['entity_id'].startswith("USR")):
                path = os.path.join(os.environ["USER_DIRECTORY"], dataset_data['entity_id'], "dataset")



            
            payload = {
                "dataset_id": self.data['dataset_id'],
                "name": self.data['name'],
                "description": self.data['description'],
                "is_public": 1,
                "created_by": self.data['owner'],
                "path": path,
                "owner": self.data['owner'],
            }

            response = self.create_subset(payload)
            return response
            
        except Exception as e:
            print("RequestCreateSubset -- do_process() Error: " + str(e))
            return "RequestCreateSubset -- do_process() Error: " + str(e)