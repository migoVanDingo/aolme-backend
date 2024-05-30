import json
import os
from flask import current_app
from api.dataset.AbstractDataset import AbstractDataset


class RequestGetFileAnnotationsByDataset(AbstractDataset):
    def __init__(self, dataset_id, filename):
        super().__init__()
        self.dataset_id = dataset_id
        self.filename = filename

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__}")

            filename = self.filename + ".json"

            # Get subset list by dataset_id
            subset_list = self.read_list_by_dataset_id(self.dataset_id)

            current_app.logger.debug(f"{self.__class__.__name__} :: subset_list: {subset_list}")

            # Get subset items by subset_id and filename
            annotation_list = self.get_annotation_list(subset_list, filename)

            current_app.logger.debug(f"{self.__class__.__name__} :: annotation_list: {annotation_list}")

            # Get annotation data by annotation_list and filename
            annotation_data = self.get_annotation_data(annotation_list, filename)

            return annotation_data

        except Exception as e:
            current_app.logger.error(
                f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__}::do_process::Error: {e}"


    def get_annotation_list(self, subset_list, filename):
        annotation_list = []
        for subset in subset_list:
            current_app.logger.debug(f"{self.__class__.__name__} :: subset: {subset['subset_id']} :: filename: {filename}")
            annotation = self.read_items_by_subset_and_filename(subset['subset_id'], filename)
            

            if "Typing" in subset['name']:
                type = "typing"
            elif "Talking" in subset['name']:
                type = "talking"
            elif "Writing" in subset['name']:
                type = "writing"
            
            annotation_list.append({ "type": type, "data":annotation[0] })
        
        return annotation_list
    
    def get_annotation_data(self, annotation_list, filename):
        annotation_data = []

        for entry in annotation_list:
            
            file_path = os.path.join(entry["data"]['path'],filename)
            current_app.logger.debug(f"{self.__class__.__name__} :: file_path: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                annotation_data.append({ "type": entry["type"], "data":data}) 

        return annotation_data
        