class Constant:

    directory_list = ['project', 'dataset', 'module', 'experiment', 'config', 'annotations','model', 'notebook', 'report', 'data', 'logs', 'ground_truth', 'dvc', 'git', 'files', 'local-storage', 'ground-truth-reformat', 'ground-truth-raw', 'videos', 'src']

   
    label_studio = {
        "webhook_actions": ["PROJECT_UPDATED"],
        "webhook_port": 5003,
        "webhook_base_url": "http://127.0.0.1:",
        "webhook_url_path": "/api/webhook-handler/project-created",
        "initialization_jobs": {
            "project":"create_label_studio_project", 
            "webhook":"create_label_studio_webhook", 
            "import-storage":"create_label_studio_import_storage", 
            "sync-import-storage":"sync_label_studio_import_storage"
        },
        "SERVICE_NAME":"LABEL_STUDIO_INTEGRATION_SERVICE"
    }

    jobs = {
        "INITIALIZE_LABEL_STUDIO": "INITIALIZE_LABEL_STUDIO",
    }



       
    
Constant.directory_list = staticmethod(Constant.directory_list)
Constant.label_studio = staticmethod(Constant.label_studio)
Constant.jobs = staticmethod(Constant.jobs)

