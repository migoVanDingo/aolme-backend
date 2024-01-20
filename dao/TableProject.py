from datetime import datetime
import random
import string
class TableProject:
    def __init__(self):
        from main import db
        self.db = db

    def generate_user_id():
        N = 22
        return 'PRJ' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    

    def insert_project(self, params):
        try:
            
            insert_query = "INSERT INTO project (project_id, name, description, owner, created_by, created_at, ls_project_id, is_public, organization, is_active) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self.db.connection.cursor()
            cur.execute(insert_query, (params['project_id'], params['name'], params['description'], params['owner'], params['created_by'], params['created_at'], int(params['ls_project_id']), params['is_public'], params["organization"], params['is_active']))
            self.db.connection.commit()
            cur.close()
            return params
        except Exception as e:
            return "Error: " + str(e)
        
    def read_project(self, project_id):
        try:
            query = "SELECT * FROM project WHERE is_active = 1 AND project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            print("Error: " + str(e))
            return "Error: " + str(e)
        

    def update_project(self, params):
        try:
            update_query = "UPDATE project SET name = %s, description = %s, owner = %s, updated_by = %s, updated_at = %s, ls_project_id = %s, is_public = %s, organization = %s WHERE is_active = 1 AND project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (params['name'], params['description'], params['owner'], params['updated_by'], params['updated_at'], params['ls_project_id'], params['is_public'], params['organization'], params['project_id']))

            self.db.connection.commit()
            cur.close()

            return params
        except Exception as e:
            return "Error: " + str(e)
        
    def archive_project(self, project_id):
        try:
            update_query = "UPDATE project SET is_active = 0 WHERE is_active = 1 AND project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (project_id,))

            self.db.connection.commit()
            cur.close()

            return project_id
        except Exception as e:
            return "Error: " + str(e)
        
    def delete_project(self, project_id):  
        try:
            delete_query = "DELETE FROM project WHERE is_active = 0 AND project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(delete_query, (project_id,))

            self.db.connection.commit()
            cur.close()

            return project_id
        except Exception as e:
            return "Error: " + str(e)

    def create_project(self, payload):
        try:
            
            now = datetime.now()

            print("TableProject.creaet_project() -- {}".format(payload))

            insert_query = "INSERT INTO project (name, description, owner, created_by, created_at, last_updated, last_updated_by, ls_project_id, is_public, organization) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self.db.connection.cursor()

            cur.execute(insert_query, (payload['name'], payload['description'], payload['owner'], payload['created_by'], now, now, payload['last_updated_by'], int(payload['ls_project_id']), 1, payload["organization"]))
            self.db.connection.commit()
            cur.close()

            response = {
                "name": payload['name'],
                "description": payload['description'],
                "owner": payload['owner'],
                "created_by": payload['created_by'],
                "created_at": now,
                "last_updated_by": payload['last_updated_by'],
                "last_updated": now,
                "ls_project_id": payload['ls_project_id']
            }

            print("TableProject.creaet_project RESPONSE() -- {}".format(response))

            return response

        except Exception as e:
            return "Error: " + str(e)
        

    def get_project_by_id(self, project_id):
        try:
            query = "SELECT * FROM project WHERE isActive = 1 AND ls_project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "Error: " + str(e)
        
    def get_project_list(self):
        try:
            query = "SELECT * FROM project WHERE isActive = 1"
            cur = self.db.connection.cursor()
            cur.execute(query)
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "Error: " + str(e)