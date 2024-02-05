import random
import string


class TableConfig:
    def __init__(self) -> None:
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'CNF' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert_config(self, payload):
        query = "INSERT INTO config (config_id, entity_id, name, description, owner, type, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"

        try:
            payload['config_id'] = self.generate_id()
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['config_id'], payload['entity_id'], payload['name'], payload['description'], payload['owner'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))
            self.db.connection.commit()
            cur.close()
            return payload
        
        except Exception as e:  
            return "TableConfig -- insert_config() Error: " + str(e)
        

    def read_list(self):
        query = "SELECT * FROM config WHERE is_active = 1 AND is_public = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableConfig -- read_list() Error: " + str(e)

    def read_item(self, config_id):
        query = "SELECT * FROM config WHERE config_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (config_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableConfig -- read_item() Error: " + str(e)
        
    def read_item_project(self, project_id):
        query = "SELECT * FROM config WHERE entity_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableConfig -- read_item_project() Error: " + str(e)
        

    def read_list_by_entity(self, entity_id):
        query = "SELECT * FROM config WHERE entity_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableConfig -- read_list_by_entity() Error: " + str(e)

    def read_list_by_user(self, user_id):
        query = "SELECT * FROM config WHERE owner = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableConfig -- read_list_by_user() Error: " + str(e)

    def update(self, payload):
        query = "UPDATE config SET name = %s, description = %s, type = %s, path = %s, is_public = %s, is_active = %s, modified_by = %s, modified_at = %s WHERE config_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['name'], payload['description'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['modified_by'], payload['modified_at'], payload['config_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            return "TableConfig -- update() Error: " + str(e)

    def delete(self, config_id):
        query = "DELETE FROM config WHERE config_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (config_id,))
            self.db.connection.commit()
            cur.close()
            return config_id
        except Exception as e:
            return "TableConfig -- delete() Error: " + str(e)

    def archive(self, config_id):
        query = "UPDATE config SET is_active = 0 WHERE config_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (config_id,))
            self.db.connection.commit()
            cur.close()
            return config_id
        except Exception as e:
            return "TableConfig -- archive() Error: " + str(e)