from enum import Enum
from pydantic import BaseModel

from flask import current_app

from utility.Utils import Utils

class JobStatus(str, Enum):
    pending = 'pending'
    in_progress = 'in-progress'
    completed = 'completed'
    failed = 'failed'

class IJobTask(BaseModel):
    job_id: str
    job_task_id: str
    task_name: str
    status: JobStatus


class TableJobTasks:
    def __init__(self):
        from main import db
        self.db = db

    def insert(self, payload: IJobTask):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {payload}")
            query = "INSERT INTO job_tasks(job_id, job_task_id, task_name, status) values (%s, %s, %s, %s)"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['job_id'], payload['job_task_id'], payload['task_name'], payload['status']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobTasks -- insert() Error: " + str(e)
        
    def get_list(self, job_id):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: job_id: {job_id}")
            query = "SELECT * FROM job_tasks WHERE job_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (job_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobTasks -- get_list() Error: " + str(e)
        
    def get_item_by_id(self, job_task_id):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: job_task_id: {job_task_id}")
            query = "SELECT * FROM job_tasks WHERE job_task_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (job_task_id,))
            data = cur.fetchall()
            cur.close()
            return data
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobTasks -- get_item_by_id() Error: " + str(e)
        
    def find_by(self, fields, values):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: fields: {fields}, values: {values}")
            query = "SELECT * FROM job_tasks WHERE "

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
            return "TableJobTasks -- find_item() Error: " + str(e)
        
    def update(self, payload):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: payload: {payload}")
            query = "UPDATE job_tasks SET status = %s WHERE job_task_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (payload['status'], payload['job_task_id']))
            self.db.connection.commit()
            cur.close()
            return payload
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "TableJobTasks -- update() Error: " + str(e)
        
    
        
