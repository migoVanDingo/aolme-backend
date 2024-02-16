from datetime import datetime
import os
class TableFiles:
    def __init__(self):
        from main import db
        self.db = db

    def make_directory_videos(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'project'), project_id)
            create_videos_dir = os.path.join(create_project_dir, 'videos')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_project_dir) is True and os.path.isdir(create_videos_dir) is not True:
                os.mkdir(create_videos_dir)
            if os.path.isdir(create_project_dir) is not True:
                os.mkdir(create_project_dir)
                os.mkdir(create_videos_dir)

            return create_videos_dir

        except OSError as e:
            return "Error: TableFiles -- make_directory_videos() --  " + str(e)
        
    def make_directory_raw_gt(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'project'), project_id)
            create_raw_gt_dir = os.path.join(create_project_dir, 'ground-truth-raw')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_project_dir) is True and os.path.isdir(create_raw_gt_dir) is not True:
                os.mkdir(create_raw_gt_dir)
            elif os.path.isdir(create_project_dir) is not True:
                os.mkdir(create_project_dir)
                os.mkdir(create_raw_gt_dir)

            return create_raw_gt_dir

        except OSError as e:
            return "Error: TableFiles -- make_directory_raw_gt() -- " + str(e)
        
    def make_directory_reformat_gt(self, project_id):
        try:
            create_project_dir = os.path.join(os.path.join(os.getcwd(), 'project'), project_id)
            create_gt_reformat_dir = os.path.join(create_project_dir, 'ground-truth-reformat')

            #create the ground truth folder if the project folder exists, else create the project folder
            if os.path.isdir(create_gt_reformat_dir) is not True:
                os.mkdir(create_gt_reformat_dir)
            

            return create_gt_reformat_dir

        except OSError as e:
            return "Error: TableFiles -- make_directory_reformat_gt() -- " + str(e)
        
    
    def create_file_info(self, payload):
        try:
            insert_query = "INSERT INTO files (project_id, path, name, extension, file_type) VALUES(%s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (int(payload['project_id']), payload['path'], payload['name'], payload['extension'], payload['file_type']))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: TableFiles -- create_file_info() -- " + str(e)
        

    def get_project_files(self, project_id):
        try:
            query = "SELECT * FROM files WHERE project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            data = list(cur.fetchall())
            cur.close()
            
            return data

        except Exception as e:
            return "Error: TableFiles -- get_project_files() -- " + str(e)
        

        
    def insert_file(self, file_name, file_content):
        try:
            insert_query = "INSERT INTO files (name, content) VALUES(%s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (file_name, file_content))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: TableFiles -- insert_file() -- " + str(e)



    def read_file(self, file_name):
        try:
            query = "SELECT content FROM files WHERE name = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (file_name,))
            data = cur.fetchone()
            cur.close()
            
            return data

        except Exception as e:
            return "Error: TableFiles -- read_file() -- " + str(e)
        


    def update_file_info(self, file_name, file_content):
        try:
            update_query = "UPDATE files SET content = %s WHERE name = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (file_content, file_name))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: TableFiles -- update_file_info() -- " + str(e)
        


    def delete_file(self, file_name):
        try:
            delete_query = "DELETE FROM files WHERE name = %s"

            cur = self.db.connection.cursor()
            cur.execute(delete_query, (file_name,))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: TableFiles -- delete_file() -- " + str(e)
        


    def archive_file(self, file_name):
        try:
            archive_query = "UPDATE files SET archived = 1 WHERE name = %s"

            cur = self.db.connection.cursor()
            cur.execute(archive_query, (file_name,))
            self.db.connection.commit()
            cur.close()

            return 'success'


        except Exception as e:
            return "Error: TableFiles -- archive_file() -- " + str(e)
    