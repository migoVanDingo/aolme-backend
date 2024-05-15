import json
import requests
import os
from datetime import datetime
from flask import current_app, jsonify
from api.label_studio.ls_project.handler.RequestExportAllFrames import RequestExportAllFrames
from api.subprocess.handler.HandleLSExportAllFrames import HandleLSExportAllFrames
from api.webhook_handler.handler.ConvertAnnotationToDataset import ConvertAnnotationToDataset


from dao.TableDatasetV2 import TableDatasetV2
from dao.TableFiles import TableFiles
from dao.TableFilesV2 import TableFilesV2
from dao.TableLsProject import TableLsProject
from dao.TableRepoItem import TableRepoItem
from dao.TableSubset import TableSubset
from dao.TableSubsetItem import TableSubsetItem


class HandleProjectUpdate:
    def __init__(self, payload):
        self.payload = json.loads(payload)

    def do_process(self):

        formatted_json_data = self.payload

        task = formatted_json_data["task"]
        task_id = task["id"]
        current_app.logger.info(f"{self.__class__.__name__} :: task_id: {task_id} :: task: {task}")


        project_id = formatted_json_data["project"]["id"]
        project_title = formatted_json_data["project"]["title"]

        ls_table = TableLsProject()
        ls_project = ls_table.read_ls_project_by_id(str(project_id))

        subset_id = ls_project['subset_id']

        table_subset = TableSubset()
        subset = table_subset.read_item(subset_id)

        table_dataset = TableDatasetV2()
        dataset = table_dataset.read_item(subset['dataset_id'])
        current_app.logger.info(f"{self.__class__.__name__} :: dataset: {dataset}")
        entity_id = dataset['entity_id']
        dataset_id = dataset['dataset_id']

        

        request_export_all_frames = HandleLSExportAllFrames(
            entity_id, dataset_id, subset_id, project_id, task_id)
        allFramesFilename = request_export_all_frames.do_process()

        if entity_id.startswith("ORG"):
            gt_processed_path = os.path.join(
                os.environ["ORGANIZATION_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "ground-truth-processed")
        elif entity_id.startswith("USR"):
            gt_processed_path = os.path.join(
                os.environ["USER_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "ground-truth-processed")
        else:
            current_app.logger.error(f"HandleProjectUpdate::::Error: Invalid entity_id: {entity_id}")
            return "HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id
        
        if entity_id.startswith("ORG"):
            annotation_path = os.path.join(
                os.environ["ORGANIZATION_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "annotation")
        elif entity_id.startswith("USR"):
            annotation_path = os.path.join(
                os.environ["USER_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "annotation")
        else:
            current_app.logger.error(f"HandleProjectUpdate::::Error: Invalid entity_id: {entity_id}")
            return "HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id

        current_app.logger.info(f"{self.__class__.__name__} :: ls_project: {ls_project}")

        with open(os.path.join(gt_processed_path, project_title+".json"), "w") as f:
            f.write(json.dumps(formatted_json_data))

        
        #add to files
        insert_file = TableFilesV2()
        payload_insert_file = {
            "entity_id": ls_project['entity_id'], 
            "name": ls_project['name'], 
            "description": ls_project['description'], "owner": ls_project['entity_id'], 
            "type": "ANNOTATION", 
            "path": gt_processed_path, 
            "is_public": 1, 
            "is_active": 1, 
            "created_by": ls_project['entity_id'], "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "entity_id": ls_project['entity_id'], 
            "name": ls_project['name'], 
            "description": ls_project['description'], "owner": ls_project['entity_id'], 
            "type": "ANNOTATION", 
            "path": gt_processed_path, 
            "is_public": 1, 
            "is_active": 1, 
            "created_by": ls_project['entity_id'], "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        current_app.logger.info(f"{self.__class__.__name__} :: payload_insert_file: {payload_insert_file}")
        response_insert_file = insert_file.insert_files(payload_insert_file)
        current_app.logger.info(f"{self.__class__.__name__} :: response_insert_file: {response_insert_file}")
  

        current_app.logger.info(f"{self.__class__.__name__} :: allFramesFilename: {allFramesFilename}")
        table_subset_item = TableSubsetItem()
        payload_subset_item = {
            "subset_id": subset_id,
            "name": allFramesFilename,
            "path": annotation_path,
            "type": "ANNOTATION",
            "is_active": 1,
            "created_by": entity_id
        }
        current_app.logger.info(f"{self.__class__.__name__} :: payload_subset_item: {payload_subset_item}")
        table_subset_item.insert(payload_subset_item)

        response_object = {
            "path": gt_processed_path,
            "project_id": project_id,
            "name": project_title.replace(" ", ""),
            # "task_id": task_id,
            "file_type": "ANNOTATION",
            "extension": "json"
        }
        current_app.logger.info(f"{self.__class__.__name__} :: response_object: {response_object}")
        self.save_file_information(response_object)
        return "SUCCESS"

    def save_file_information(self, data):
        table_files = TableFiles()
        return table_files.create_file_info(data)
