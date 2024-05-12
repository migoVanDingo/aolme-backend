import json
import os

from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset

class RequestGetSubsetAnnotation(AbstractDataset):
    def __init__(self, subset_id, filename):
        super().__init__()
        # self.subset_id = subset_id
        # self.dataset_id = dataset_id
        # self.entity_id = entity_id
        self.filename = filename
        self.subset_id = subset_id
        
    def do_process(self):
        try:


            # if self.entity_id.startswith("ORG"):
            #     path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id)
            # elif self.entity_id.startswith("USR"):
            #     path = os.path.join(os.environ["USER_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id)

            # annotation_dir = os.path.join(path, "annotation")
            current_app.logger.info(f"{self.__class__.__name__} :: subset_id: {self.subset_id}")
            subset = self.read_subset(self.subset_id)
            path = subset['path']
            annotation_path = os.path.join(path, "annotation")
            current_app.logger.info(f"{self.__class__.__name__} :: annotation_path: {annotation_path}")

            filename = self.filename.split(".")
            filename = filename[0] + ".json"

            current_app.logger.info(f"{self.__class__.__name__} :: filename: {filename}")

            #read annotation dir
            files = os.listdir(annotation_path)
            for file in files:
                current_app.logger.info(f"{self.__class__.__name__} :: file: {file}")
                #read file
                if file == filename:
                    with open(os.path.join(annotation_path,filename), 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        current_app.logger.info(f"{self.__class__.__name__} :: response: {data}")
                        return data
                    
            return "RequestGetSubsetAnnotation::do_process::Error: File not found"

            
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetSubsetAnnotation::do_process::Error: {}".format(e)