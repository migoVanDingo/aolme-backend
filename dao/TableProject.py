from datetime import datetime
class TableProject:
    def __init__(self):
        from main import db
        self.db = db
        

    def create_project(self, payload):
        try:
            
            now = datetime.now()

            insert_query = "INSERT INTO project (name, description, owner, created_by, created_at, last_updated, last_updated_by, ls_project_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self.db.connection.cursor()

            cur.execute(insert_query, (payload['name'], payload['description'], payload['owner'], payload['created_by'], now, now, payload['last_updated_by'], int(payload['ls_project_id'])))
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

            return response

        except Exception as e:
            return "Error: " + str(e)
        

    def get_project_by_id(self, project_id):
        try:
            query = "SELECT * FROM project WHERE isActive = 1 AND id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id))
            
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