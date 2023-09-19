from datetime import datetime
import os
class TableFiles:
    def __init__(self):
        from main import db
        self.db = db

    def make_directory_videos(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'uploads'), project_id)
            create_videos_dir = os.path.join(create_project_dir, 'videos')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_project_dir) is True and os.path.isdir(create_videos_dir) is not True:
                os.mkdir(create_videos_dir)
            if os.path.isdir(create_project_dir) is not True:
                os.mkdir(create_project_dir)
                os.mkdir(create_videos_dir)

            return create_videos_dir

        except OSError as e:
            return "Error: " + str(e)
        
    def make_directory_raw_gt(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'uploads'), project_id)
            create_raw_gt_dir = os.path.join(create_project_dir, 'ground-truth-raw')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_project_dir) is True and os.path.isdir(create_raw_gt_dir) is not True:
                os.mkdir(create_raw_gt_dir)
            elif os.path.isdir(create_project_dir) is not True:
                os.mkdir(create_project_dir)
                os.mkdir(create_raw_gt_dir)

            return create_raw_gt_dir

        except OSError as e:
            return "Error: " + str(e)
        
    def make_directory_reformat_gt(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'uploads'), project_id)
            create_gt_reformat_dir = os.path.join(create_project_dir, 'ground-truth-reformat')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_gt_reformat_dir) is not True:
                os.mkdir(create_gt_reformat_dir)
            

            return create_gt_reformat_dir

        except OSError as e:
            return "Error: " + str(e)
        
    
    def create_file_info(self, payload):
        try:
            insert_query = "INSERT INTO files (project_id, path, name, extension, file_type) VALUES(%s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (int(payload['project_id']), payload['path'], payload['name'], payload['extension'], payload['file_type']))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: " + str(e)
        

    def get_project_files(self, project_id):
        try:
            query = "SELECT * FROM files WHERE project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            data = list(cur.fetchall())
            cur.close()
            
            return data

        except Exception as e:
            return "Error: " + str(e)