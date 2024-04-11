from api.label_studio.ls_project.AbstractLsProject import AbstractLsProject

class RequestExportAllFrames(AbstractLsProject):
    def __init__(self, project_id):
        self.project_id = project_id

    def do_process(self):
        url = self.endpoint_url_get_all_frames(self.project_id)
        response = self.get(url, self.get_headers()).json()

        return response