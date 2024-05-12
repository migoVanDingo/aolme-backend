from flask import current_app
import requests
class FileUtility:
    def __init__(self):
        pass

    def signal_reformat_xlsx(repo_id, file_set_id):
        try:
            url = 'http://localhost:3002/convert/xlsx/{}/{}'.format(repo_id, file_set_id)
            x = requests.get(url)

            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::signal_reformat_xlsx::Error: " + str(e))
            return "Error: " + str(e)
        
    def signal_reformat_xlsx_v3(entity_id, dataset_id, subset_id, file_set_id):
        try:
            url = 'http://localhost:3002/convert/xlsx/entity/{}/dataset/{}/subset/{}/file_set_id/{}'.format(entity_id, dataset_id, subset_id, file_set_id)
            x = requests.get(url)

            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::signal_reformat_xlsx_v3::Error: " + str(e))
            return "FileUtility::Error: " + str(e)
        
    def signal_reformat_xlsx_v2(path):
        try:
            headers = {
            "Content-Type": "application/json"
            }
            data={
                "path": path
            }
            url = 'http://localhost:3002/convert/v2/xlsx'
            x = requests.post(url, data=data, headers=headers)

            current_app.logger.info("FileUtility::signal_reformat_xlsx_v2(): {}".format(x.json()))
            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::Error: " + str(e))
            return "Error: " + str(e)
        
    def signal_create_local_storage(project_id, repo_id):
        try:
            url = 'http://localhost:3002/local-storage/{}/{}'.format(project_id, repo_id)
            x = requests.get(url)
            current_app.logger.info("FileUtility::signal_create_local_storage(): {}".format(x.json()))
            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::signal_create_local_storage::Error: " + str(e))
            return "Error: " + str(e)
        

    def move_files_to_local_storage(project_id, repo_id):
        print('CALL: move_files_to_local_storage')
        try:
            
            url = 'http://localhost:3002/local-storage/{}/move/{}'.format(project_id, repo_id)
            print(url)
            x = requests.get(url)


            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::move_files_to_local_storage::Error: " + str(e))  
            return "Error: " + str(e)
        
    def move_files_to_local_storage_v2(entity_id, dataset_id, subset_id):
        print('CALL: move_files_to_local_storage_v2')
        try:
            
            url = 'http://localhost:3002/local-storage/entity/{}/dataset/{}/subset/{}/move'.format( entity_id, dataset_id, subset_id)
            print(url)
            x = requests.get(url)


            return x.json()
        except Exception as e:
            current_app.logger.error("FileUtility::move_files_to_local_storage_v2::Error: " + str(e))
            return "Error: " + str(e)
        
