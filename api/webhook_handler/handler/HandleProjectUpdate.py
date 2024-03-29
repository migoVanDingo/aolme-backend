import json, requests, os
from datetime import datetime
from flask import jsonify
from api.webhook_handler.handler.ConvertAnnotationToDataset import ConvertAnnotationToDataset
from dao.TableDataset import TableDataset

from dao.TableFiles import TableFiles
from dao.TableLsProject import TableLsProject
from dao.TableRepoItem import TableRepoItem
class HandleProjectUpdate:
    def __init__(self, payload):
        self.payload = json.loads(payload)

    def do_process(self):
      
        

        formatted_json_data = self.payload

        print("Formatted JSON Data: {}".format(formatted_json_data))
        
        project_id = formatted_json_data["project"]["id"]
        project_title = formatted_json_data["project"]["title"]

        ls_table = TableLsProject()
        ls_project = ls_table.read_ls_project_by_id(str(project_id))

        print("LS Project: {}".format(ls_project))

        repo_directory = os.path.join(os.environ['REPO_DIRECTORY'], ls_project['repo_id'])
        annotation_directory = os.path.join(repo_directory, 'annotations')

        if os.path.exists(annotation_directory) == False:
            os.mkdir(annotation_directory)

        final_path = os.path.join(annotation_directory, project_title)
        with open(final_path, "w") as f:
            f.write(json.dumps(formatted_json_data))

        ### Convert JSON to CSV
        request_convert_annotation = ConvertAnnotationToDataset(formatted_json_data, project_id, project_title, final_path)
        response_convert_annotation = request_convert_annotation.do_process()

       

        
        #add to files
        insert_file = TableDataset()
        payload_insert_file = {
             "entity_id": ls_project['entity_id'], "name": ls_project['name'], "description": ls_project['description'], "owner": ls_project['entity_id'], "type":"ANNOTATION", "path": final_path, "is_public": 1, "is_active":1, "created_by":ls_project['entity_id'], "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        response_insert_file = insert_file.insert_files(payload_insert_file)

        repo_item = TableRepoItem()
        payload_repo_item = {
            "file_id": response_insert_file["file_id"],
            "repo_id": ls_project['repo_id'],
            "type": "ANNOTATION",
            "is_active": 1,
            "created_by": ls_project['entity_id'],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
        }
        response_repo_item = repo_item.insert(payload_repo_item)

        print("Response Insert File: {}".format(response_repo_item))


        response_object = {
                    "path": final_path,
                    "project_id": project_id,
                    "name": project_title.replace(" ", ""),
                    #"task_id": task_id,
                    "file_type": "ANNOTATION",
                    "extension": "json"
                }

        self.save_file_information(response_object)
        return "SUCCESS"


       
                
        

    
    def save_file_information(self, data):
        table_files = TableFiles()
        return table_files.create_file_info(data)