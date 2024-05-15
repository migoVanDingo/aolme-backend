from datetime import datetime
import os

from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
from api.dataset.entity.CreateDatasetValidator import CreateDatasetValidator
from dao.TableDatasetV2 import TableDatasetV2
from dao.TableRepoItem import TableRepoItem

class RequestCreateDataset(AbstractDataset):
    def __init__(self,data):
        super().__init__()
        self.data = data
        

    def do_process(self):
        try:
            
            self.data['path'] = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], self.data['entity_id'], self.data['name'])
            # Validate the payload
            validator = CreateDatasetValidator()
            is_valid = validator.validate(self.data)
            if is_valid[0] is False:
                current_app.logger.error(f"{self.__class__.__name__} :: do_process() Error: {is_valid[1]}")
                return is_valid[1]
            
    
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.data}")
            response = self.create(self.data)
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            
            return response
            

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: do_process() Error: {str(e)}")
            return "RequestCreateDataset -- do_process() Error: " + str(e)