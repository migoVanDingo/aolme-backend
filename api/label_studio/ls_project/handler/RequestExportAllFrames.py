from flask import current_app
from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestExportAllFrames(AbstractLsProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        try:
            current_app.logger.info(f"{self.__class__.__name__} :: project_id: {self.project_id}")
            url = self.endpoint_url_get_all_frames(self.project_id)

            current_app.logger.info(f"{self.__class__.__name__} :: url: {url}")
            response = self.get(url, self.get_headers()).json()
            current_app.logger.info(f"{self.__class__.__name__} :: Response: {response}")

            return response
        
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404