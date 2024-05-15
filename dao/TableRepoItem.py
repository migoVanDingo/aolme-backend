from datetime import datetime

from flask import current_app


class TableRepoItem:
    def __init__(self):
        from main import db
        self.db = db

    def insert(self, payload):
        query = "INSERT INTO repo_item(file_id, repo_id, type, is_active, created_at, created_by) values(%s, %s, %s, %s, %s, %s)"

        try:
            payload['is_active'] = 1
            payload['created_at'] = "{}".format(datetime.now())
            payload['created_by'] = payload['created_by'] if 'created_by' in payload else payload['owner'] if 'owner' in payload else payload['user_id'] if 'user_id' in payload else "DATA_ERROR_USER_ID"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['file_id'], payload['repo_id'], payload['type'], payload['is_active'], payload['created_at'], payload['created_by']))
            self.db.connection.commit()
            cur.close()

            current_app.logger.debug(f"{self.__class__.__name__} :: insert-repo-item :: payload: {payload}")

            return payload
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: insert-repo-item :: Error: {str(e)}")
            return "TableRepoItem -- insert() Error: " + str(e)
        
    def archive(self, repo_item_id):
        query = "UPDATE repo_item SET is_active = 0 WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_item_id,))
            self.db.connection.commit()
            cur.close()
            return "SUCCESS"
        except Exception as e:
            return "TableRepoItem -- archive() Error: " + str(e)
        
    def delete(self, repo_item_id): 
        query = "DELETE FROM repo_item WHERE file_id = %s"
        try:
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_item_id,))
            self.db.connection.commit()
            cur.close()
            return "SUCCESS"
        except Exception as e:
            return "TableRepoItem -- delete() Error: " + str(e)
        

    def read_list_repo_items(self, repo_id):
        
        try:
            query = "SELECT * FROM repo_item WHERE is_active = 1 AND repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_id,))
            data = cur.fetchall()
            cur.close()
            
            return data

            

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: read_list_repo_items :: Error: {str(e)}")
            return f"{self.__class__.__name__} :: read_list_repo_items :: Error: {str(e)}"