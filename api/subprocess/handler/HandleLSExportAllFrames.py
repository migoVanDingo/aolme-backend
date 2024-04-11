import os
import subprocess
from dao.TableSubset import TableSubset


class HandleLSExportAllFrames():
    def __init__(self, entity_id, dataset_id, subset_id, project_id, task_id):
        self.entity_id = entity_id
        self.dataset_id = dataset_id
        self.subset_id = subset_id
        self.project_id = project_id
        self.task_id = task_id

    def do_process(self):
        table_subset = TableSubset()
        subset = table_subset.read_item(self.subset_id)
        name = subset['name']
        name = name.replace(" ", "")

        if self.entity_id.startswith("ORG"):
            path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id, "annotation")
        elif self.entity_id.startswith("USR"):
            path = os.path.join(os.environ["USER_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id, "annotation")
        else:
            print("HandleProjectUpdate::::Error: Invalid save path")
            return "HandleProjectUpdate::::Error: Invalid save path"
        

        #Export the file to the ground-truth-processed directory
        os.chdir(path)

        commands = [
            "curl -X GET 'http://localhost:8080/api/projects/" + str(self.project_id) + "/export?exportType=JSON&interpolate_key_frames=true&ids[]=" + str(self.task_id) + "' -H 'Authorization: Token " + os.environ['LABEL_STUDIO_SECRET_KEY'] + "' --output " + name + ".json"
        ]
        
        for command in commands:
            subprocess.run(command, shell=True, check=True)

        
