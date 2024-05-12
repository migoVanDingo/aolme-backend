import os

from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset
from dao.TableDatasetV2 import TableDatasetV2
from dao.TableSubsetItem import TableSubsetItem
class RequestCreateSubset(AbstractDataset):
    def __init__(self,data,files):
        super().__init__()
        self.data = data
        self.files = files
        
    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: payload: {self.data}")
            dataset = TableDatasetV2()
            dataset_data = dataset.read_item(self.data['dataset_id'])

            path = ""
            if(dataset_data['entity_id'].startswith("ORG")):
                path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], dataset_data['entity_id'], "dataset")
            elif(dataset_data['entity_id'].startswith("USR")):
                path = os.path.join(os.environ["USER_DIRECTORY"], dataset_data['entity_id'], "dataset")

            
            path = os.path.join(path, self.data['dataset_id'])
            
            if not os.path.exists(path):
                os.mkdir(path) 

            
            path = os.path.join(path, "subset")
            current_app.logger.info(f"{self.__class__.__name__} :: path: {path}")
            if not os.path.exists(path):
                os.mkdir(path) 


            payload = {
                "dataset_id": self.data['dataset_id'],
                "name": self.data['name'],
                "description": self.data['description'],
                "is_public": 1,
                "created_by": self.data['owner'],
                "path": path,
                "owner": self.data['owner'],
            }

            current_app.logger.info(f"{self.__class__.__name__} :: create-subset-payload: {payload}")

            response = self.create_subset(payload)
            current_app.logger.info(f"{self.__class__.__name__} :: create-subset-response: {response}")


            if not os.path.exists(response['path']):
                    os.mkdir(response['path'])

            subset_paths = ["annotation", "files", "misc", "dataset", "xlsx", "local-storage", "ground-truth-raw", "ground-truth-processed"]

            for subset_path in subset_paths:
                if not os.path.exists(os.path.join(response['path'], subset_path)):
                    os.mkdir(os.path.join(response['path'], subset_path))

            dao_subset_item = TableSubsetItem()
                
            for file in self.files:
                f = file.filename
                name = f.split('.')
                extension = name[1]

                file_save_payload = {
                    "subset_id": response['subset_id'],
                    "created_by": self.data['owner'], 
                      
                }


                if extension == "xlsx":
                    filepath = os.path.join(response['path'], "xlsx")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "XLSX"
                    current_app.logger.info(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                    dao_subset_item.insert(file_save_payload)
                    file.save(os.path.join(filepath, f))

                
                elif extension == "json" or extension == "txt" or extension == "csv":

                    filepath = os.path.join(response['path'], "annotation")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "ANNOTATION"
                    current_app.logger.info(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                    dao_subset_item.insert(file_save_payload)
                    file.save(os.path.join(filepath, f))



                elif extension == "jpg" or extension == "jpeg" or extension == "png" or extension == "gif":
                    
                    filepath = os.path.join(response['path'], "files")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "IMAGE"
                    current_app.logger.info(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                    file.save(os.path.join(filepath, f))
                    dao_subset_item.insert(file_save_payload)

                elif  extension == "mp4" or extension == "mov" or extension == "mpg":
                    filepath = os.path.join(response['path'], "files")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "VIDEO"
                    current_app.logger.info(f"{self.__class__name__} :: file_save_payload: {file_save_payload}")
                    file.save(os.path.join(filepath, f))
                    dao_subset_item.insert(file_save_payload)

            

                elif extension == "mp3" or extension == "wav": 
                    filepath = os.path.join(response['path'], "files")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "AUDIO"
                    current_app.logger.info(f"{self.__class__name__} :: file_save_payload: {file_save_payload}")
                    file.save(os.path.join(filepath, f))
                    dao_subset_item.insert(file_save_payload)

                else:
                    filepath = os.path.join(response['path'], "misc")
                    file_save_payload['path'] = filepath
                    file_save_payload['name'] = f
                    file_save_payload["type"] = "MISC"
                    current_app.logger.info(f"{self.__class__.__name__} :: file_save_payload: {file_save_payload}")
                    file.save(os.path.join(filepath, f))    
                    dao_subset_item.insert(file_save_payload)               
        
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")
            return response
            
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: do_process() Error: {str(e)}")
            return "RequestCreateSubset -- do_process() Error: " + str(e)