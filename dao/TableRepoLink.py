from datetime import datetime
import logging
import random
import string

from flask import current_app, jsonify

class TableRepoLink:

    def __init__(self):
        from main import db
        self.db = db
    
    def insert(self, payload, dir_name):
        try:
            query = "INSERT INTO repo_link (repo_id, link, dir_name, type, path, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"

            payload['is_active'] = 1
            payload['created_at'] = f"{datetime.now()}"
            payload['created_by'] = payload['user_id']
            payload['dir_name'] = dir_name

            cur = self.db.connection.cursor()
            cur.execute(query, (payload["repo_id"], payload["github_url"], payload['dir_name'], payload["type"], payload['path'], payload["is_active"], payload["created_at"], payload["created_by"]))

            self.db.connection.commit()

            return payload
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableRepoLink -- insert_repository: " + str(e)
        finally:
            cur.close()

    def read(self, repo_id):
        try:
            query = "SELECT * FROM repo_link WHERE is_active = 1 AND repo_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (repo_id,))
            
            data = cur.fetchall()

            cur.close()

            
            return data
        except Exception as e:
            return "TableRepoLink -- read_repository: " + str(e)