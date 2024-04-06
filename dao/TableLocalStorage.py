import datetime


class TableLocalStorage():
    def __init__(self, db):
        from main import db
        self.db = db

    
    def insert_export_storage(self, payload):
        try:
            insert_query = "INSERT INTO export_storage (path , title, project_id, entity_id, user_id, is_active, created_at, created_by, updated_at, updated_by, deleted_at, deleted_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['path'], payload['title'], payload['project_id'], payload['entity_id'], payload['user_id'], payload['is_active'], payload['created_at'], payload['created_by'], payload['updated_at'], payload['updated_by'], payload['deleted_at'], payload['deleted_by']))

            self.db.connection.commit()
            cur.close()

            return payload


        except Exception as e:
            return datetime.now() + "TableLocalStorage -- insert_export_storage() Error: " + str(e)

    def read_export_storage(self, project_id):
        try:
            query = "SELECT * FROM export_storage WHERE is_active = 1 AND project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return datetime.now() + ": TableLocalStorage -- read_export_storage: " + str(e)

    def update_export_storage(self, payload):
        try:
            query = "UPDATE export_storage SET path = %s, title = %s, project_id = %s, entity_id = %s, user_id = %s, is_active = %s, created_at = %s, created_by = %s, updated_at = %s, updated_by = %s, deleted_at = %s, deleted_by = %s WHERE export_storage_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['path'], payload['title'], payload['project_id'], payload['entity_id'], payload['user_id'], payload['is_active'], payload['created_at'], payload['created_by'], payload['updated_at'], payload['updated_by'], payload['deleted_at'], payload['deleted_by'], payload['export_storage_id']))

            self.db.connection.commit()
            cur.close()
        
            return payload
        
        except Exception as e:
            return datetime.now() + "TableLocalStorage -- update_export_storage() Error: " + str(e)

    def delete_export_storage(self, project_id):
        try:
            query = "UPDATE export_storage SET is_active = 0 WHERE project_id = %s"
            cur = self.db.connection.cursor()

            cur.execute(query, (project_id,))
            self.db.connection.commit()
            cur.close()

            return project_id
        except Exception as e:
            return datetime.now() + "TableLocalStorage -- delete_export_storage() Error: " + str(e)


    def insert_import_storage(self, payload):
        try:
            insert_query = "INSERT INTO import_storage (path , title, project_id, entity_id, user_id, is_active, created_at, created_by, updated_at, updated_by, deleted_at, deleted_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload['path'], payload['title'], payload['project_id'], payload['entity_id'], payload['user_id'], payload['is_active'], payload['created_at'], payload['created_by'], payload['updated_at'], payload['updated_by'], payload['deleted_at'], payload['deleted_by']))

            self.db.connection.commit()
            cur.close()

            return payload

        except Exception as e:
            return datetime.now() + "TableLocalStorage -- insert_import_storage() Error: " + str(e)
        
    def read_import_storage(self, project_id):
        try:
            query = "SELECT * FROM import_storage WHERE is_active = 1 AND project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (project_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return datetime.now() + ": TableLocalStorage -- read_import_storage: " + str(e)
        

    def update_import_storage(self, project_id, payload):
        try:
            query = "UPDATE import_storage SET path = %s, title = %s, project_id = %s, entity_id = %s, user_id = %s, is_active = %s, created_at = %s, created_by = %s, updated_at = %s, updated_by = %s, deleted_at = %s, deleted_by = %s WHERE project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(query, (payload['path'], payload['title'], payload['project_id'], payload['entity_id'], payload['user_id'], payload['is_active'], payload['created_at'], payload['created_by'], payload['updated_at'], payload['updated_by'], payload['deleted_at'], payload['deleted_by'], project_id))

            self.db.connection.commit()
            cur.close()

            return payload
        except Exception as e:
            return datetime.now() + "TableLocalStorage -- update_import_storage() Error: " + str(e)
        


    def delete_import_storage(self, project_id):
        try:
            query = "UPDATE import_storage SET is_active = 0 WHERE project_id = %s"
            cur = self.db.connection.cursor()

            cur.execute(query, (project_id,))
            self.db.connection.commit()
            cur.close()

            return project_id
        except Exception as e:
            return datetime.now() + "TableLocalStorage -- delete_import_storage() Error: " + str(e)
        

    