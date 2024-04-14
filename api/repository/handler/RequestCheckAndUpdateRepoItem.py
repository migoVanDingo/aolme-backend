from datetime import datetime

from flask import jsonify
from api.repository.AbstractRepository import AbstractRepository
from dao.TableRepoItem import TableRepoItem

class RequestCheckAndUpdateRepoItem(AbstractRepository):
    def __init__(self, data, repo_id):
        super().__init__()
        self.repo_id = repo_id
        self.data = data

    def do_process(self):
        try:
            table_repo_item = TableRepoItem()
            query = "SELECT * FROM repo_item WHERE repo_id = %s AND is_active = 1"
            cur = table_repo_item.db.connection.cursor()
            cur.execute(query, (self.repo_id,))
            data = cur.fetchall()
            cur.close()

            response = data

            print("RequestCheckAndUpdateRepoItem -- do_process() data: ", data)

            if data and len(data) > 0 and "file_id" in data[0]:
                query = "UPDATE repo_item SET type = %s, updated_by = %s, updated_at = %s, file_id = %s WHERE repo_id = %s and is_active = 1"
                cur = table_repo_item.db.connection.cursor()
                cur.execute(query, (self.data['file_type'], self.data['user_id'], "{}".format(datetime.now()), self.data['file_id'], self.repo_id))
                table_repo_item.db.connection.commit()
                cur.close()

                print('\nhere1\n')

            else:
                print('here2')
                self.data['created_at'] = "{}".format(datetime.now())
                self.data['created_by'] = self.data['user_id']
                self.data['is_active'] = 1
                query = "INSERT INTO repo_item(file_id, repo_id, type, is_active, created_at, created_by) values(%s, %s, %s, %s, %s, %s)"
                cur = table_repo_item.db.connection.cursor()
                cur.execute(query, (self.data['file_id'], self.repo_id, self.data['file_type'], self.data['is_active'], self.data['created_at'], self.data['created_by']))
                table_repo_item.db.connection.commit()
                cur.close()
                response = self.data

            print("RequestCheckAndUpdateRepoItem -- do_process() Success: ", response)

            return jsonify(response)
        
        except Exception as e:
            print("RequestCheckAndUpdateRepoItem -- do_process() Error: " + str(e))
            return "RequestCheckAndUpdateRepoItem -- do_process() Error: " + str(e)