import json

from incoming import datatypes, PayloadValidator

class ProjectPayloads:

    @classmethod
    def create_task_payload(self, data):
        title = data["title"] if data["title"] is not None else None
        description = data["description"] if data["description"] is not None else 'none'
        label_config = data["label_config"] if data["label_config"] else ''
        expert_instruction = data["expert_instruction"] if data["expert_instruction"] else ''
        show_instruction = data["show_instruction"] if data["show_instruction"] else True
        show_skip_button = data["show_skip_button"] if data["show_skip_button"] else True
        enable_empty_annotation = data["enable_empty_annotation"] if data["enable_empty_annotation"] else True
        show_annotation_history = data["show_annotation_history"] if data["show_annotation_history"] else True
        organization = data["organization"] if data["organization"] else 0
        color = data["color"] if data["color"] else ''
        maximum_annotations = data
        ["maximum_annotations"] if data["maximum_annotations"] else 0
        is_published = data["is_published"] if data["is_published"] else True
        model_version = data["model_version"] if data["model_version"] else ''
        is_draft = data["is_draft"] if data["is_draft"] else True

        created_by = data["created_by"]

        min_annotations_to_start_training = data["min_annotations_to_start_training"] if data[
            "min_annotations_to_start_training"] else 0

        show_collab_predictions = data["show_collab_predictions"] if data["show_collab_predictions"] else True
        sampling = data["sampling"] if data["sampling"] else ''
        show_ground_truth_first = data["show_ground_truth_first"] if data["show_ground_truth_first"] else True

        show_overlap_first = data["show_overlap_first"] if data["show_overlap_first"] else True
        overlap_cohort_percentage = data["overlap_cohort_percentage"] if data["overlap_cohort_percentage"] else 0
        task_data_login = data["task_data_login"] if data["task_data_login"] else ''

        task_data_password = data["task_data_password"] if data["task_data_password"] else ''
        control_weights = data["control_weights"]
        evaluate_predictions_automatically = data["evaluate_predictions_automatically"] if data[
            "evaluate_predictions_automatically"] else True

        skip_queue = data["skip_queue"] if data["skip_queue"] else ''
        reveal_preannotations_interactively = data["reveal_preannotations_interactively"] if data[
            "reveal_preannotations_interactively"] else True
        pinned_at = data["pinned_at"] if data["pinned_at"] else ''

        response_payload = {
            "title": title,
            "description": description,
            "label_config": label_config,
            "expert_instruction": expert_instruction,
            "show_instruction": show_instruction,
            "show_skip_button": show_skip_button,
            "enable_empty_annotation": enable_empty_annotation,
            "show_annotation_history": show_annotation_history,
            "organization": organization,
            "color": color,
            "maximum_annotations": maximum_annotations,
            "is_published": is_published,
            "model_version": model_version,
            "is_draft": is_draft,
            "created_by": created_by,
            "min_annotations_to_start_training": min_annotations_to_start_training,
            "show_collab_predictions": show_collab_predictions,
            "sampling": sampling,
            "show_ground_truth_first": show_ground_truth_first,
            "show_overlap_first": show_overlap_first,
            "overlap_cohort_percentage": overlap_cohort_percentage,
            "task_data_login": task_data_login,
            "task_data_password": task_data_password,
            "control_weights": {},
            "evaluate_predictions_automatically": evaluate_predictions_automatically,
            "skip_queue": skip_queue,
            "reveal_preannotations_interactively": reveal_preannotations_interactively,
            "pinned_at": pinned_at
        }

        return response_payload

