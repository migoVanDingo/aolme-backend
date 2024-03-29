import csv
import json
import os
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject
class ConvertAnnotationToDataset(AbstractLsProject):
    def __init__(self, annotation, project_id, project_title, path):
        self.annotation = annotation
        self.project_id = project_id
        self.project_title = project_title
        self.path = path
     

    def do_process(self):
        url = self.endpoint_url_get_all_frames(self.project_id)
        response = self.get(url, self.get_headers()).json()

        print("Response length: {}".format(len(response)))

        rows = []
        for task in response:
            task_id = task['id']
            file_path = task['data']['video']
            #file_name = task['file_upload']
            
            for annotation in task['annotations']:
                project_id = annotation['project']
                task_id = annotation['task']

                for result in annotation['result']:
                    label_arr = result['value']['labels']
                    label = label_arr[0]

                    for frame in result['value']['sequence']:
                        frame['task_id'] = task_id
                        frame['file_path'] = file_path
                        #frame['file_name'] = file_name
                        frame['project_name'] = self.project_title
                        frame['label'] = label
                        frame['project_id'] = project_id

                        rows.append(frame)
                    #END FOR frame IN sequence

        #END FOR task IN response
                        
        csv_filename = "{}.csv".format(self.path)
        #csv_filename = os.path.join(self.path, csv_filename)
        print("CSV Filename: {}".format(csv_filename))

        with open(csv_filename, 'w', newline='') as csvfile:
            # Extract field names from the first item in the JSON data
            fieldnames = list(rows[1].keys())

            # Create a CSV writer and write the header
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            # Write each row to the CSV file
            for row in rows:
                writer.writerow(row)





                
        return

        


    