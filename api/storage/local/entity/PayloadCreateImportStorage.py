from incoming import datatypes, PayloadValidator
class PayloadCreateImportStorage(PayloadValidator):
    path = datatypes.String(required=True)
    regex_filter = datatypes.String(required=False)
    title = datatypes.String(required=True)
    description = datatypes.String(required=False)
    last_sync = datatypes.String(required=False)
    last_sync_job = datatypes.String(required=False)

    use_blob_urls = datatypes.Boolean(required=False)

    last_sync_count = datatypes.Integer(required=False)
    project = datatypes.Integer(required=True)