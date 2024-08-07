import os
from api.repository.AbstractRepository import AbstractRepository
from flask import current_app, jsonify

class RequestGetRepoStages(AbstractRepository):
    def __init__(self, path):
        super().__init__()
        self.path = path
        

    def do_process(self):
        current_app.logger.debug(f"{self.__class__.__name__} :: Fetching repository stages :: path: {self.path}")

        try:
            path = os.path.join(self.path, "model", "stages")
            items = os.listdir(path)
            stages = []
            for item in items:
                if os.path.isfile(os.path.join(path, item)):
                    stages.append(item)
            
            current_app.logger.debug(f"{self.__class__.__name__} :: Fetching repository stages :: stages: {stages}")
            return jsonify(stages)

        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return "RequestGetRepoStages -- do_process: " + str(e)