import json
from flask import current_app, jsonify
from request.request import Request
from dao.TableJobTasks import TableJobTasks
from dao.TableJobs import TableJobs
from utility.Utils import Utils
from utility.Constant import Constant


class RequestInitializeLabelStudioForDatastore:

    def __init__(self, payload):
        self.payload = payload
        self.job_tracking_db = TableJobs()
        self.job_task_db = TableJobTasks()


    def do_process(self):
        current_app.logger.debug(f"{self.__class__.__name__} :: payload: {self.payload}")
        payload_insert_job = {
            "data": json.dumps(self.payload),
            "job_name": Constant.jobs["INITIALIZE_LABEL_STUDIO"],
            "service": "LABEL_STUDIO_INTEGRATION_SERVICE",
            "tasks": json.dumps([
                Constant.label_studio["initialization_jobs"]["project"], 
                Constant.label_studio["initialization_jobs"]["webhook"]]),
            "status": "pending",
            

        }
 
        # Constant.label_studio["initialization_jobs"]["import-storage"], 
        # Constant.label_studio["initialization_jobs"]["sync-import-storage"]
        # Insert Job into jobs table
        insert_job = self.job_tracking_db.insert(payload_insert_job)

        # Notify LabelStudio Integration Service
        Request.get_request(url="http://localhost:5005/api/label_studio/job", headers={ "Content-Type": "application/json" })


        current_app.logger.debug(f"{self.__class__.__name__} :: insert_job response: {insert_job}")



        return insert_job
