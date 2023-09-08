from incoming import datatypes, PayloadValidator
class PayloadCreateWebhook(PayloadValidator):
    project = datatypes.Integer(required=True)
    url = datatypes.String(required=True)
    send_payload = datatypes.Boolean(required=True)
    headers = datatypes.Function('validate_headers', required=False)
    is_active = datatypes.Boolean(required=True)
    actions = datatypes.Function('validate_action', required=True)


    @classmethod
    def validate_headers(self,val, **kwargs):
        if val is None:
            return False
        return True
    
    @classmethod
    def validate_action(self,val, **kwargs):
        if val is None:
            return False
        return True