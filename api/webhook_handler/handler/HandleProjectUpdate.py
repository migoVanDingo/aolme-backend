import json
import requests
import os
from datetime import datetime
from flask import jsonify
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

        print("Task: {}".format(task))
        print("Task ID: {}".format(task_id))

        # print("Formatted JSON Data: {}".format(formatted_json_data))

        project_id = formatted_json_data["project"]["id"]
        project_title = formatted_json_data["project"]["title"]

        ls_table = TableLsProject()
        ls_project = ls_table.read_ls_project_by_id(str(project_id))

        subset_id = ls_project['subset_id']

        table_subset = TableSubset()
        subset = table_subset.read_item(subset_id)

        table_dataset = TableDatasetV2()
        dataset = table_dataset.read_item(subset['dataset_id'])
        print("HandleProjectUpdate::dataset: {}".format(dataset))
        entity_id = dataset['entity_id']
        dataset_id = dataset['dataset_id']

        print("HandleProjectUpdate::task_id: {}".format(task_id))

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
            print("HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id)
            return "HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id
        
        if entity_id.startswith("ORG"):
            annotation_path = os.path.join(
                os.environ["ORGANIZATION_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "annotation")
        elif entity_id.startswith("USR"):
            annotation_path = os.path.join(
                os.environ["USER_DIRECTORY"], entity_id, "dataset", dataset_id, "subset", subset_id, "annotation")
        else:
            print("HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id)
            return "HandleProjectUpdate::::Error: Invalid entity_id: " + entity_id

        print("LS Project: {}".format(ls_project))

        with open(os.path.join(gt_processed_path, project_title+".json"), "w") as f:
            f.write(json.dumps(formatted_json_data))

        # Convert JSON to CSV
        # request_convert_annotation = ConvertAnnotationToDataset(formatted_json_data, project_id, project_title, gt_processed_path)
        # response_convert_annotation = request_convert_annotation.do_process()

       

        
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

        response_insert_file = insert_file.insert_files(payload_insert_file)

        # repo_item = TableRepoItem()
        # payload_repo_item = {
        #     "file_id": response_insert_file["file_id"],
        #     "repo_id": ls_project['repo_id'],
        #     "type": "ANNOTATION",
        #     "is_active": 1,
        #     "created_by": ls_project['entity_id'],
        #     "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # }
        # response_repo_item = repo_item.insert(payload_repo_item)

        # print("Response Insert File: {}".format(response_repo_item))

        print("HandleProjectUpdate::allFramesFilename: {}".format(allFramesFilename))
        print("HandleProjectUpdate::allFramesFilename: {}".format(allFramesFilename))
        table_subset_item = TableSubsetItem()
        payload_subset_item = {
            "subset_id": subset_id,
            "name": allFramesFilename,
            "path": annotation_path,
            "type": "ANNOTATION",
            "is_active": 1,
            "created_by": entity_id
        }

        table_subset_item.insert(payload_subset_item)

        response_object = {
            "path": gt_processed_path,
            "project_id": project_id,
            "name": project_title.replace(" ", ""),
            # "task_id": task_id,
            "file_type": "ANNOTATION",
            "extension": "json"
        }

        self.save_file_information(response_object)
        return "SUCCESS"

    def save_file_information(self, data):
        table_files = TableFiles()
        return table_files.create_file_info(data)
