import random
import string


class TableDataset:
    def __init__(self):
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'DS' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert_dataset(self, payload):
        query = "INSERT INTO dataset(dataset_id, entity_id, name, description, owner, type, path, is_public, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        try:
            payload['dataset_id'] = self.generate_id()
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['dataset_id'], payload['entity_id'], payload['name'], payload['description'], payload['owner'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['created_by'], payload['created_at']))
            self.db.connection.commit()
            cur.close()
            return payload
        
        except Exception as e:  
            print("TableDataset -- insert_dataset() Error: " + str(e))
            return "TableDataset -- insert_dataset() Error: " + str(e)
        

    def read_list(self):
        query = "SELECT * FROM dataset WHERE is_active = 1 AND is_public = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableDataset -- read_list() Error: " + str(e)
        

    def read_item(self, dataset_id):
        query = "SELECT * FROM dataset WHERE dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (dataset_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableDataset -- read_item() Error: " + str(e)

    def read_list_by_entity(self, entity_id):
        query = "SELECT * FROM dataset WHERE entity_id = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableDataset -- read_list_by_entity() Error: " + str(e)

    def read_list_by_user(self, user_id):
        query = "SELECT * FROM dataset WHERE owner = %s AND is_active = 1"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableDataset -- read_list_by_user() Error: " + str(e)
        

    def update(self, payload):
        query = "UPDATE dataset SET name = %s, description = %s, type = %s, path = %s, is_public = %s, is_active = %s, modified_by = %s, modified_at = %s WHERE dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['name'], payload['description'], payload['type'], payload['path'], payload['is_public'], payload['is_active'], payload['modified_by'], payload['modified_at'], payload['dataset_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            return "TableDataset -- update() Error: " + str(e)

    def delete(self, dataset_id):
        query = "DELETE FROM dataset WHERE dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (dataset_id,))
            self.db.connection.commit()
            cur.close()
            return dataset_id
        except Exception as e:
            return "TableDataset -- delete() Error: " + str(e)

    def archive(self, dataset_id):
        query = "UPDATE dataset SET is_active = 0 WHERE dataset_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (dataset_id,))
            self.db.connection.commit()
            cur.close()
            return dataset_id
        except Exception as e:
            return "TableDataset -- archive() Error: " + str(e)