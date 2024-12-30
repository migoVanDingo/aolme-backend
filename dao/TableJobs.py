from flask import current_app
from utility.Utils import Utils
from enum import Enum
from pydantic import BaseModel

class JobStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in-progress'
    completed = 'completed'
    failed = 'failed'

class IJob(BaseModel):
    job_name: str
    data: str



class TableJobs:
    def __init__(self):
        from main import db
        self.db = db

    def insert(self, payload):
        try:

            payload['job_id'] = Utils.generate_id("JOB")
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {payload}")
            
            query = "INSERT INTO jobs(job_id, job_name, data, tasks, service) values (%s, %s, %s, %s, %s)"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['job_id'], payload['job_name'], payload['data'], payload['tasks'], payload['service']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobs -- insert() Error: " + str(e)
        
    def get_list(self):
        try:
            query = "SELECT * FROM jobs"
            cur = self.db.connection.cursor()
            cur.execute(query)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobs -- get_list() Error: " + str(e)
        
    def get_item_by_id(self, job_id):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: job_id: {job_id}")
            query = "SELECT * FROM jobs WHERE job_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (job_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobs -- get_item_by_id() Error: " + str(e)
        

    def find_by(self, fields, values):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: fields: {fields}, values: {values}")
            query = "SELECT * FROM jobs WHERE "
            for i in range(len(fields)):
                query += fields[i] + " = %s"
                if i < len(fields) - 1:
                    query += " AND "
            cur = self.db.connection.cursor()
            cur.execute(query, values)
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobs -- find_by() Error: " + str(e)
        
    def update(self, payload):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {payload}")
            query = "UPDATE jobs SET job_name = %s, payload = %s, status = %s, updated_at = %s WHERE job_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['job_name'], payload['payload'], payload['status'], payload['updated_at'], payload['job_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobs -- update() Error: " + str(e)
        

