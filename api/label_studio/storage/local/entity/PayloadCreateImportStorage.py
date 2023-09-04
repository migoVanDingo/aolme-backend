from incoming import datatypes, PayloadValidator
class PayloadCreateImportStorage(PayloadValidator):
    #Required Parameters
    path = datatypes.String(required=True)
    project = datatypes.Integer(required=True)
    title = datatypes.String(required=True)

    #Nullable
    regex_filter = datatypes.String(required=False)
    description = datatypes.String(required=False)
    last_sync = datatypes.String(required=False)
    last_sync_job = datatypes.String(required=False)
    use_blob_urls = datatypes.Boolean(required=False)
    last_sync_count = datatypes.Integer(required=False)
    

    