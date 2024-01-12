import random
import string


class TableEntityGroup:
    def __init__(self):
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'EGR' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    def insert_entity(self, payload):
        insert_query = "INSERT INTO entity_group (entity_group_id, entity_id, name, access, entity_type, active_from, active_to, entity_status, is_primary, is_active, created_by, created_at) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)"

        try:
            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['entity_group_id'], payload['entity_id'], payload['name'], payload['access'], payload['entity_type'], payload['active_from'], payload['active_to'], payload['entity_status'], payload['is_primary'], payload['is_active'], payload['created_by'], payload['created_at']))
            self.db.connection.commit()
            cur.close()
            return payload
        
        except Exception as e:
            return "TableEntityGroup -- insert_entity() Error: " + str(e)
        
    def get_entity_group_by_id(self, entity_group_id):
        try:
            query = "SELECT * FROM entity_group WHERE entity_group_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_group_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableEntityGroup -- get_entity_group_by_id() Error: " + str(e)
        
    def get_entity_group_by_entity_id(self, entity_id):
        try:
            query = "SELECT * FROM entity_group WHERE entity_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableEntityGroup -- get_entity_group_by_entity_id() Error: " + str(e)
        
    def get_entity_list_by_type(self, entity_type):
        try:
            query = "SELECT * FROM entity_group WHERE entity_type = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_type,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            return "TableEntityGroup -- get_entity_list_by_type() Error: " + str(e)
        
    def update_entity_group(self, payload):
        try:
            query = "UPDATE entity_group SET name = %s, access = %s, entity_type = %s, active_from = %s, active_to = %s, entity_status = %s, is_primary = %s, is_active = %s, modified_by = %s, modified_at = %s WHERE entity_group_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['name'], payload['access'], payload['entity_type'], payload['active_from'], payload['active_to'], payload['entity_status'], payload['is_primary'], payload['is_active'], payload['modified_by'], payload['modified_at'], payload['entity_group_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            return "TableEntityGroup -- update_entity_group() Error: " + str(e)
        
        
    def archive_entity_group(self, entity_group_id):
        try:
            query = "UPDATE entity_group SET is_active = 0 WHERE entity_group_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_group_id,))
            self.db.connection.commit()
            cur.close()
            return entity_group_id
        except Exception as e:
            return "TableEntityGroup -- archive_entity_group() Error: " + str(e)
        
    def delete_entity_group(self, entity_group_id):
        try:
            query = "DELETE FROM entity_group WHERE entity_group_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_group_id,))
            self.db.connection.commit()
            cur.close()
            return entity_group_id
        except Exception as e:
            return "TableEntityGroup -- delete_entity_group() Error: " + str(e)
        
    