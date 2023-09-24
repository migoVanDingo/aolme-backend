import json, requests, os

from dao.TableFiles import TableFiles
class HandleProjectUpdate:
    def __init__(self, payload):
        self.payload = json.loads(payload)

    def do_process(self):
        data = self.payload
        project_id = data['project']['id']
        project_title = data['project']['title']
        #task_id = data['task']['id']

        formatted_json_data = json.dumps(self.payload, indent=4)

        
        uploads_dir = os.path.join(os.getcwd(), 'project')
        project_dir = os.path.join(uploads_dir, str(project_id))
        if os.path.exists(project_dir) == False:
             os.mkdir(project_dir)

        annotation_directory = os.path.join(project_dir, 'annotations')

        if os.path.exists(annotation_directory) == False:
            os.mkdir(annotation_directory)

        final_path = os.path.join(annotation_directory, project_title)

        with open(final_path, "w") as f:
                    f.write(formatted_json_data)

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