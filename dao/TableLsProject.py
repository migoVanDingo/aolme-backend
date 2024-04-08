from datetime import datetime
import random
import string
import json

from flask import jsonify

class TableLsProject:
    def __init__(self):
        from main import db
        self.db = db

    def generate_id(self):
        N = 22
        return 'LSP' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=N))
    
    def insert_ls_project(self, params):
        try:
            params['ls_id'] = self.generate_id()
            query = "INSERT INTO label_studio_project(ls_id, ls_project_id, entity_id, subset_id, name, description, is_active, created_by, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            cur = self.db.connection.cursor()
            cur.execute(query, (params['ls_id'], params['ls_project_id'], params['entity_id'], params['subset_id'],params['name'], params['description'], params['is_active'], params['created_by'], params['created_at']))

            self.db.connection.commit()
            cur.close()
            return params
        except Exception as e:
            print("Error::TableLsProject::insert_ls_project(): " + str(e))
            return "Error::TableLsProject::insert_ls_project(): " + str(e)

    def insert_ls_project_info(self, params):
        try:
            params['ls_project_id'] = self.generate_id()
            insert_query = "INSERT INTO label_studio_project_info (ls_project_id, entity_id, title, description, label_config, expert_instruction, color, model_version, sampling, task_data_login, task_data_password, skip_queue, pinned_at, organization, maximum_annotations, overlap_cohort_percentage, show_instructions, show_skip_button, enable_empty_annotation, show_annotation_history, is_published, is_draft, show_collab_predictions, show_ground_truth_first, show_overlap_first, is_active, created_by, created_at, updated_by, updated_at, deleted_by, deleted_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

            cur = self.db.connection.cursor()

            cur.execute(insert_query, (params['ls_project_id'], params['entity_id'] , params['title'], params['description'], params['label_config'], params['expert_instruction'], params['color'], params['model_version'], params['sampling'], params['task_data_login'], params['task_data_password'], params['skip_queue'], params['pinned_at'], params['organization'], params['maximum_annotations'], params['overlap_cohort_percentage'], params['show_instructions'], params['show_skip_button'], params['enable_empty_annotation'], params['show_annotation_history'], params['is_published'], params['is_draft'], params['show_collab_predictions'], params['show_ground_truth_first'], params['show_overlap_first'], params['is_active'], params['created_by'], params['created_at'], params['updated_by'], params['updated_at'], params['deleted_by'], params['deleted_at']))

            self.db.connection.commit()
            cur.close()
            return params
        except Exception as e:
            return "Error::TableLsProject::insert_ls_project(): " + str(e)
        
    def read_ls_project_by_id(self, ls_project_id):
        try:
            query = "SELECT * FROM label_studio_project WHERE is_active = 1 AND ls_project_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (ls_project_id,))
            
            data = cur.fetchall()

            cur.close()

            return data[0]
        except Exception as e:
            return "Error::TableLsProject::read_ls_project_by_id(): " + str(e)
        
    def read_ls_project_by_subset_id(self, subset_id):
        try:
            query = "SELECT * FROM label_studio_project WHERE is_active = 1 AND subset_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (subset_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "Error::TableLsProject::read_ls_project_by_subset_id(): " + str(e)
        
    def read_ls_project_list_by_entity_id(self, entity_id):
        try:
            query = "SELECT * FROM ls_project WHERE is_active = 1 AND entity_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (entity_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "Error::TableLsProject::read_ls_project_list_by_entity_id(): " + str(e)
        
    def read_ls_project_list_by_dataset_id(self, dataset_id):
        try:
            query = "SELECT * FROM ls_project WHERE is_active = 1 AND dataset_id = %s"
            cur = self.db.connection.cursor()
            cur.execute(query, (dataset_id,))
            
            data = cur.fetchall()

            cur.close()

            return data
        except Exception as e:
            return "Error::TableLsProject::read_ls_project_list_by_dataset_id(): " + str(e)
        

    def update_ls_project(self, params):
        try:
            update_query = "UPDATE ls_project_id SET title = %s, description = %s, label_config = %s, expert_instruction = %s, color = %s, model_version = %s, sampling = %s, task_data_login = %s, task_data_password = %s, skip_queue = %s, pinned_at = %s, organization = %s, maximum_annotations = %s, overlap_cohort_percentage = %s, show_instructions = %s, show_skip_button = %s, enable_empty_annotation = %s, show_annotation_history = %s, is_published = %s, is_draft = %s, show_collab_predictions = %s, show_ground_truth_first = %s, show_overlap_first = %s, is_active = %s, updated_by = %s, updated_at = %s WHERE is_active = 1 AND ls_project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (params['title'], params['description'], params['label_config'], params['expert_instruction'], params['color'], params['model_version'], params['sampling'], params['task_data_login'], params['task_data_password'], params['skip_queue'], params['pinned_at'], params['organization'], params['maximum_annotations'], params['overlap_cohort_percentage'], params['show_instructions'], params['show_skip_button'], params['enable_empty_annotation'], params['show_annotation_history'], params['is_published'], params['is_draft'], params['show_collab_predictions'], params['show_ground_truth_first'], params['show_overlap_first'], params['is_active'], params['updated_by'], params['updated_at'], params['ls_project_id']))

            self.db.connection.commit()
            cur.close()

            return params
        except Exception as e:
            return "Error::TableLsProject::update_ls_project(): " + str(e)
        
    def archive_ls_project(self, ls_project_id):
        try:
            update_query = "UPDATE ls_project SET is_active = 0 WHERE is_active = 1 AND ls_project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(update_query, (ls_project_id,))

            self.db.connection.commit()
            cur.close()

            return ls_project_id
        except Exception as e:
            return "Error::TableLsProject::archive_ls_project(): " + str(e)
        
    def delete_ls_project(self, ls_project_id):
        try:
            delete_query = "DELETE FROM ls_project WHERE ls_project_id = %s"

            cur = self.db.connection.cursor()
            cur.execute(delete_query, (ls_project_id,))

            self.db.connection.commit()
            cur.close()

            return ls_project_id
        except Exception as e:
            return "Error::TableLsProject::delete_ls_project(): " + str(e)