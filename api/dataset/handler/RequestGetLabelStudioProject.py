from flask import current_app, jsonify
from api.dataset.AbstractDataset import AbstractDataset
from dao.TableLsProject import TableLsProject

class RequestGetLabelStudioProject(AbstractDataset):
    def __init__(self, subset_id):
        self.subset_id = subset_id
        self.table_label_studio_project = TableLsProject()

    def do_process(self):
        try:
            current_app.logger.debug(f"{self.__class__.__name__} :: subset_id: {self.subset_id}")

            response = self.table_label_studio_project.read_ls_import_storage_by_subset_id(self.subset_id)
            
            current_app.logger.debug(f"{self.__class__.__name__} :: Response: {response}")
            return response
        except Exception as e:
            current_app.logger.error(f"{self.__class__.__name__} :: ERROR: {str(e)}")
            return f"{self.__class__.__name__} :: ERROR: {str(e)}", 404