from datetime import datetime
import os
class TableFiles:
    def __init__(self):
        from main import db
        self.db = db

    def make_directory(self, project_id):
        try:
            #filename = payload['filename'].split(".")
            create_dir = os.path.join(os.path.join(os.getcwd(), 'uploads'), project_id)
            os.mkdir(create_dir)

            create_dir = os.path.join(create_dir, 'videos')
            os.mkdir(create_dir)

            return create_dir

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
        
    
