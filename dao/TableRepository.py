from datetime import datetime
import logging
import random
import string

class TableRepository:

    def __init__(self):
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'RPS' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert(self, payload):
        try:
            payload["repo_id"] = self.generate_id()
            query = "INSERT INTO repository (repo_id, name, description, owner, entity_id, is_public, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload["repo_id"], payload["name"], payload["description"], payload["owner"], payload['entity_id'] , payload["is_public"], payload["is_active"], payload["created_at"], payload["created_by"]))

            self.db.connection.commit()

            return payload
        
        except Exception as e:
            print("TableRepository -- insert_repository: " + str(e))
            return "TableRepository -- insert_repository: " + str(e)
        finally:
            cur.close()

    def read(self, id):
        try:
            query = "SELECT * FROM repository WHERE is_active = 1 AND repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (id,))
            
            data = cur.fetchall()

            cur.close()

            

            return data[0]
        except Exception as e:
            return "TableRepository -- read_repository: " + str(e)
        
    
    def read_list_owner(self, owner):
        try:
            query = "SELECT * FROM repository WHERE is_active = 1 AND owner = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (owner,))   

            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return datetime.now() + ": TableRepository -- read_repository: " + str(e)
        
    def read_list_entity(self, entity_id):
        try:
            query = "SELECT * FROM repository WHERE is_active = 1 AND entity_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))   

            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return datetime.now() + ": TableRepository -- read_repository: " + str(e)
        
    
    def update(self, payload):
        try:
            query = "UPDATE repository SET name = %s, description = %s, is_public = %s, is_active = %s, updated_at = %s, updated_by = %s WHERE repo_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload["name"], payload["description"], payload["is_public"], payload["is_active"], payload["updated_at"], payload["updated_by"], payload["repo_id"]))

            self.db.connection.commit()

            return payload
        except Exception as e:
            return datetime.now() + ": TableRepository -- update_repository: " + str(e)
        finally:
            cur.close()


    def archive(self, id):
        try:
            query = "UPDATE repository SET is_active = 0 WHERE repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (id,))
            self.db.connection.commit()
            cur.close()

            return id
        except Exception as e:
            return datetime.now() + ": TableRepository -- archive_repository: " + str(e)
        finally:
            cur.close()

    
    def delete(self, id):
        try:
            query = "DELETE FROM repository WHERE repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (id,))
            self.db.connection.commit()
            cur.close()

            return id
        except Exception as e:
            return datetime.now() + ": TableRepository -- delete_repository: " + str(e)
        finally:
            cur.close() 




    







    

