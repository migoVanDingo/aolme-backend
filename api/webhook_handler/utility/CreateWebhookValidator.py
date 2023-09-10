from incoming import datatypes, PayloadValidator
class CreateWebhookValidator(PayloadValidator):
    url = datatypes.String(required=True)

    project = datatypes.Integer(required=False)

    send_for_all_actions = datatypes.Boolean(required=True)
    send_payload = datatypes.Boolean(required=True)
    is_active = datatypes.Boolean(required=True)

    headers = datatypes.Function('validate_headers', required=True)
    actions = datatypes.Function('validate_actions', required=True)