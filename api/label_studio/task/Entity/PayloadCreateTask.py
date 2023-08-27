from incoming import datatypes, PayloadValidator
class PayloadCreateTask(PayloadValidator):
    overlap = datatypes.Integer(required=False)
    inner_id = datatypes.Integer(required=False)
    total_annotations = datatypes.Integer(required=False)
    cancelled_annotations = datatypes.Integer(required=False)
    total_predictions = datatypes.Integer(required=False)
    comment_count = datatypes.Integer(required=False)
    unresolved_comment_count = datatypes.Integer(required=False)
    project = datatypes.Integer(required=False)
    updated_by = datatypes.Integer(required=False)
    file_upload = datatypes.Integer(required=False)

    is_labeled = datatypes.Boolean(required=False)
    last_comment_updated_at: datatypes.String(required=False)

    data = datatypes.Function('validate_data', required=True)
    meta = datatypes.Function('validate_meta', required=False)
    comment_authors = datatypes.Function('validate_comment_authors', required=False)

    @classmethod
    def validate_data(self,val, **kwargs):
        if val is None:
            return False
        return True
    
    @classmethod
    def validate_meta(self,val, **kwargs):
        if val is None:
            return False
        return True
    
    @classmethod
    def validate_comment_authors(self,val, **kwargs):
        if val is None:
            return False
        return True