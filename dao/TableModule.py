import random
import string


class TableModule:
    def __init__(self) -> None:
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'MOD' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert_module(self, payload):
        query = "INSERT INTO module (module_id, entity_id, name, description, owner, type, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"

        try:
            payload['module_id'] = self.generate_id()
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['module_id'], payload['entity_id'], payload['name'], payload['description'], payload['owner'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))
            self.db.connection.commit()
            cur.close()
            return payload
        
        except Exception as e:  
            return "TableModule -- insert_module() Error: " + str(e)
        

    def read_list(self):
        query = "SELECT * FROM module WHERE is_active = 1 AND is_public = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableModule -- read_list() Error: " + str(e)

    def read_item(self, module_id):
        query = "SELECT * FROM module WHERE module_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (module_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableModule -- read_item() Error: " + str(e)

    def read_list_by_entity(self, entity_id):
        query = "SELECT * FROM module WHERE entity_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableModule -- read_list_by_entity() Error: " + str(e)

    def read_list_by_user(self, user_id):
        query = "SELECT * FROM module WHERE owner = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableModule -- read_list_by_user() Error: " + str(e)
        
    def read_list_project(self, project_id):
        query = "SELECT * FROM module WHERE project_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableModule -- read_list_project() Error: " + str(e)

    def update(self, payload):
        query = "UPDATE module SET name = %s, description = %s, type = %s, path = %s, is_public = %s, is_active = %s, modified_by = %s, modified_at = %s WHERE module_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['name'], payload['description'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['modified_by'], payload['modified_at'], payload['module_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            return "TableModule -- update() Error: " + str(e)

    def delete(self, module_id):
        query = "DELETE FROM module WHERE module_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (module_id,))
            self.db.connection.commit()
            cur.close()
            return module_id
        except Exception as e:
            return "TableModule -- delete() Error: " + str(e)

    def archive(self, module_id):
        query = "UPDATE module SET is_active = 0 WHERE module_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (module_id,))
            self.db.connection.commit()
            cur.close()
            return module_id
        except Exception as e:
            return "TableModule -- archive() Error: " + str(e)