from datetime import datetime


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

            print("TableRepoItem -- insert() Success: ", payload)

            return payload
        
        except Exception as e:
            print("TableRepoItem -- insert() Error: " + str(e))
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

            """ result = []
            for item in repo_item_data:
                #print("item: ", item)
                res = None

                query = "SELECT * FROM files WHERE file_id = %s AND is_active = 1"
                cur = self.db.connection.cursor()
                cur.execute(query, (item['file_id'],))
                res = cur.fetchall()
                cur.close()
                result.append(res[0]) 
                match item['type']:
                    case "DATASET":
                        query = "SELECT * FROM dataset WHERE dataset_id = %s AND is_active = 1"
                        cur = self.db.connection.cursor()
                        cur.execute(query, (item['repo_item_id'],))
                        res = cur.fetchall()
                        cur.close()
                        
                        
                    case "CONFIG":
                        query = "SELECT * FROM config WHERE config_id = %s AND is_active = 1"
                        cur = self.db.connection.cursor()
                        cur.execute(query, (item['repo_item_id'],))
                        res = cur.fetchall()
                        cur.close()
                        
                    case "MODULE":
                        query = "SELECT * FROM module WHERE module_id = %s AND is_active = 1"
                        cur = self.db.connection.cursor()
                        cur.execute(query, (item['repo_item_id'],))
                        res = cur.fetchall()
                        cur.close()
                        
                    case _:
                        print("Invalid type")

                
            
            print("result: ", result)
            return result """

        except Exception as e:
            print("TableRepoItem -- read_list_repo_item() Error: " + str(e))
            return "TableRepoItem -- read_list_repo_item() Error: " + str(e)