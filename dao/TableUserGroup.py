import random
import string


class TableUserGroup:
    def __init__(self):
        from main import db
        self.db = db

    def generate_id():
        N = 22
        return 'UGP' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))

    def insert_user_group(self, payload):    
        try:
            insert_query = "INSERT INTO user_group(user_group_id, name, description, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['user_group_id'], payload['name'], payload['description'], payload['is_active'], payload['created_at'], payload['created_by']))

            self.db.connection.commit()
            cur.close()

            return payload
        
        except Exception as e:
            return "Error: TableUserGroup -- insert_user_group() -- " + str(e)
        

    def read_user_group(self, user_group_id):
        try:
            query = "SELECT * FROM user_group WHERE is_active = 1 AND user_group_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (user_group_id,))
            data = cur.fetchone()
            cur.close()
            
            return data

        except Exception as e:
            return "Error: TableUserGroup -- read_user_group() -- " + str(e)
        
    def update_user_group(self, payload):
        try:
            update_query = "UPDATE user_group SET name = %s, description = %s, updated_at = %s, updated_by = %s WHERE is_active = 1 AND user_group_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (payload['name'], payload['description'], payload['updated_at'], payload['updated_by'], payload['user_group_id']))

            self.db.connection.commit()
            cur.close()

            

            return payload
        except Exception as e:
            return "Error: TableUserGroup -- update_user_group() -- " + str(e)
        

    def delete_user_group(self, user_group_id):
        try:
            delete_query = "DELETE FROM user_group WHERE user_group_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(delete_query, (user_group_id,))
            self.db.connection.commit()
            cur.close()

            return 'success'

        except Exception as e:
            return "Error: TableUserGroup -- delete_user_group() -- " + str(e)
        

    def archive_user_group(self, user_group_id):
        try:
            archive_query = "UPDATE user_group SET is_active = 0 WHERE user_group_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(archive_query, (user_group_id,))
            self.db.connection.commit()
            cur.close()

            return 'success'

        except Exception as e:
            return "Error: TableUserGroup -- archive_user_group() -- " + str(e)