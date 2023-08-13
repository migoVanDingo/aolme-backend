import json

from incoming import datatypes, PayloadValidator
class ProjectValidator(PayloadValidator):
    title = datatypes.String(required=False)
    description = datatypes.String(required=False)
    label_config = datatypes.String(required=False)
    expert_instruction = datatypes.String(required=False) 
    color = datatypes.String(required=False)
    model_version = datatypes.String(required=False)
    sampling = datatypes.String(required=False)
    task_data_login = datatypes.String(required=False)
    task_data_password = datatypes.String(required=False)
    skip_queue = datatypes.String(required=False)
    pinned_at = datatypes.String(required=False)

    organization = datatypes.Integer(required=False)
    maximum_annotations = datatypes.Integer(required=False)
    overlap_cohort_percentage = datatypes.Integer(required=False)

    show_instruction = datatypes.Boolean(required=False)
    show_skip_button = datatypes.Boolean(required=False)
    enable_empty_annotation = datatypes.Boolean(required=False)
    show_annotation_history = datatypes.Boolean(required=False)
    is_published = datatypes.Boolean(required=False)
    is_draft = datatypes.Boolean(required=False)
    show_collab_predictions = datatypes.Boolean(required=False)
    show_ground_truth_first = datatypes.Boolean(required=False)
    show_overlap_first = datatypes.Boolean(required=False)

    # control_weights = datatypes.Function('validate_control_weights', required=False)
    # created_by = datatypes.Function('validate_created_by', required=False)

    @classmethod
    def validate_control_weights(self,val,**kwargs):
        if val is None:
            return False
        return True
    @classmethod
    def validate_created_by(self,val,**kwargs):
        if val is None:
            return False
        return True