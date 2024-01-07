from datetime import datetime
import random
import string

class TableOrganization:
    def __init__(self):
        from main import db
        self.db = db

    def generate_org_id():
        N = 22
        return 'ORG' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


    def insert_organization(self, payload):
      
        try:
            org_id = self.generate_org_id()

            insert_query = "INSERT INTO organization (organization_id, name, url, description, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s)"

            
            cur = self.db.connection.cursor()
            cur.execute(insert_query, (org_id, payload['name'], payload['url'], payload['description'], payload['is_active'], payload['created_at'], payload['created_by']))

            self.db.connection.commit()
            cur.close()

            response = {
                "organization_id":org_id,
                "name": payload['name'],
                "url":payload['url'],
                "description": payload['description'],
                "created_at": payload['created_at'],
                "created_by": payload['created_by']
            }

            return response
        except Exception as e:
            return "TableOrganization -- create_organization() Error: " + str(e)
        

        
    def read_organization(self, org_id):
        try:
            query = "SELECT * FROM organization WHERE is_active = 1 AND organization_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (org_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return datetime.now() + ": TableOrganization -- read_organization: " + str(e)
        


    def update_organization(self, params):
        try:
            query = "UPDATE organization SET name = %s, url = %s, description = %s WHERE organization_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (params['name'], params['url'], params['description'], params['org_id']))
            self.db.connection.commit()
            cur.close()

            return params
        except Exception as e:
            return "TableOrganization -- update_organization() Error: " + str(e)


    def archive_organization(self, org_id):
        try:
            query = "UPDATE organization SET is_active = 0 WHERE organization_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (org_id,))
            self.db.connection.commit()
            cur.close()

            return org_id
        except Exception as e:
            return "TableOrganization -- archive_organization() Error: " + str(e)
        

    def delete_organization(self, org_id):
        try:
            query = "DELETE FROM organization WHERE organization_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (org_id,))
            self.db.connection.commit()
            cur.close()

            return org_id
        except Exception as e:
            return "TableOrganization -- delete_organization() Error: " + str(e)