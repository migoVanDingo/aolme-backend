from datetime import datetime
import logging
import random
import string

import MySQLdb

class TableOrganization:
    def __init__(self):
        from main import db
        self.db = db

    def generate_org_id(self):
        N = 22
        return 'ORG' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))


    def insert_organization(self, payload):
      
        try:

            insert_query = "INSERT INTO organization (organization_id, name, email, description, is_active, created_at, created_by) VALUES(%s, %s, %s, %s, %s, %s, %s)"

            payload["org_id"] = self.generate_org_id()

            #print(payload)
            
            cur = self.db.connection.cursor()
            cur.execute(insert_query, (payload["org_id"], payload["name"], payload["email"], payload["description"], payload["is_active"], payload["created_at"], payload["created_by"]))

            self.db.connection.commit()


            return payload
        except MySQLdb.IntegrityError:
            logging.warn("failed to insert values %d, %s", id, "TABLE_ORG::INSERT_ORG")
        except Exception as e:
            print(str(e))
            return "TableOrganization -- create_organization() Error: " + str(e)
        finally:
            cur.close()
       
        

        
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
        

    def read_organization_by_user_id(self, user_id):
        try:
            query = "SELECT * FROM organization WHERE is_active = 1 AND created_by = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (user_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "TableOrganization -- read_organization_by_user_id() Error: " + str(e)
        


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