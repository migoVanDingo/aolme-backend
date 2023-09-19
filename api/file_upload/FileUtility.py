import requests
class FileUtility:
    def __init__(self):
        pass

    def signal_reformat_xlsx(project_id):
        try:
            url = 'http://localhost:3002/convert/xlsx/{}'.format(project_id)
            x = requests.get(url)

            return x.json()
        except Exception as e:
            return "Error: " + str(e)
        
    def signal_create_local_storage(project_id):
        try:
            url = 'http://localhost:3002/local-storage/{}'.format(project_id)
            x = requests.get(url)
            print('signal_create_local_storage()')
            return x.json()
        except Exception as e:
            return "Error: " + str(e)
        

    def move_files_to_local_storage(project_id):
        print('CALL: move_files_to_local_storage')
        try:
            
            url = 'http://localhost:3002/local-storage/{}/move'.format(project_id)
            print(url)
            x = requests.get(url)


            return x.json()
        except Exception as e:
            return "Error: " + str(e)
    
