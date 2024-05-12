import json
import os
import subprocess
import time

from flask import current_app
from dao.TableSubset import TableSubset


class HandleLSExportAllFrames():
    def __init__(self, entity_id, dataset_id, subset_id, project_id, task_id):
        self.entity_id = entity_id
        self.dataset_id = dataset_id
        self.subset_id = subset_id
        self.project_id = project_id
        self.task_id = task_id

    def do_process(self):
        current_app.logger.info(f"{self.__class__.__name__} :: entity_id: {self.entity_id} :: dataset_id: {self.dataset_id} :: subset_id: {self.subset_id} :: project_id: {self.project_id} :: task_id: {self.task_id}")

        table_subset = TableSubset()
        subset = table_subset.read_item(self.subset_id)
        name = subset['name']
        name = name.replace(" ", "")

        if self.entity_id.startswith("ORG"):
            path = os.path.join(os.environ["ORGANIZATION_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id, "annotation")
        elif self.entity_id.startswith("USR"):
            path = os.path.join(os.environ["USER_DIRECTORY"], self.entity_id, "dataset", self.dataset_id, "subset", self.subset_id, "annotation")
        else:
            current_app.logger.error(f"{self.__class__.__name__} :: Error: Invalid entity_id: {self.entity_id}")
            return "HandleProjectUpdate::::Error: Invalid save path"
        

        #Export the file to the ground-truth-processed directory
        os.chdir(path)
        current_app.logger.info(f"{self.__class__.__name__} :: path: {path}")

        commands = [
            "curl -X GET 'http://localhost:8080/api/projects/" + str(self.project_id) + "/export?exportType=JSON&interpolate_key_frames=true&ids[]=" + str(self.task_id) + "' -H 'Authorization: Token " + os.environ['LABEL_STUDIO_SECRET_KEY'] + "' --output " + name + ".json"
        ]
        current_app.logger.info(f"{self.__class__.__name__} :: commands: {commands}")
        
        for command in commands:
            subprocess.run(command, shell=True, check=True)

        response = self.changeFilename("{}.json".format(name))
        current_app.logger.info(f"{self.__class__.__name__} :: response: {response}")

        return response

    
    def changeFilename(self, name):
        #check current directory for files
        current_app.logger.info(f"{self.__class__.__name__} :: changeFileName(): {name}")
        files = os.listdir()
        for file in files:
            if file == name:
                #read file
                with open(file, 'r') as f:
                    data = f.read()
                    #get the video string of the data object in the first element
                    
                    videoPath = json.loads(data)
                    videoPath = videoPath[0]['data']
                    videoPath = videoPath['video']
                    current_app.logger.info(f"{self.__class__.__name__} :: videoPath: {videoPath}")

                    #split the video string by the / character
                    videoPath = videoPath.split('/')
                    #get the last element of the split string
                    videoName = videoPath[-1]
                    #rename the file to the video name

                    videoName = videoName.split('.')[0]
                    videoName = videoName + ".json"

                    os.rename(file, videoName)

                    current_app.logger.info(f"{self.__class__.__name__} :: changeFilesName:: videoName: {videoName}")
                    return videoName





        
