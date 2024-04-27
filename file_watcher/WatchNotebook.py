from genericpath import isfile
from os import listdir
import os
import time
from dao.TableFilesV2 import TableFilesV2

from dao.TableFiles import TableFiles
from dao.TableRepoItem import TableRepoItem


class WatchNotebook:
    def __init__(self):
        pass

    def watch(self, path):
        print("Watching notebook directory: " + path)


    def fileInDirectory(self, watchDirectory: str):
        items = []
        with os.scandir(watchDirectory) as it:
            for entry in it:
                if not entry.name.startswith('.'):
                    if entry.is_file():
                        file_name = entry.name
                        base_name, extension = os.path.splitext(file_name)
                        if extension == ".ipynb" or extension == ".py":
                            items.append(file_name)

        return items
        

    def listComparison(self, existing_db_files: list, new_files: list):
        return [x for x in new_files if x not in existing_db_files] 
    

    def fileWatcher(self, watchDirectory: str, pollTime: int, payload_insert_file):
        print("Watching notebook directory: " + watchDirectory)
        while True:
        
            #Get from database
            table_files = TableFilesV2()
            previousFileList = table_files.read_list_by_entity(payload_insert_file['entity_id'])

            print("Previous File List 1: {}".format(previousFileList))
            previousFileList = [x['name'] for x in previousFileList]
            print("Previous File List 2: {}".format(previousFileList))

            #Check project directory
            newFileList = self.fileInDirectory(watchDirectory)
            print("New File List: {}".format(newFileList))
            
            fileDiff = self.listComparison(previousFileList, newFileList)

            for file in fileDiff:
                payload_insert_file['name'] = file
                payload_insert_file['path'] = os.path.join(watchDirectory, file)
                payload_insert_file['created_at'] = time.strftime("%Y-%m-%d %H:%M:%S")
                payload_insert_file['created_by'] = payload_insert_file['owner']

                print("Payload Insert File: {}".format(payload_insert_file))
                response_insert_file = table_files.insert_files(payload_insert_file)
                print("Response Insert File: {}".format(response_insert_file))

                table_repo_item = TableRepoItem()
                payload_repo_item = {
                    "file_id": response_insert_file["file_id"],
                    "repo_id": payload_insert_file['repo_id'],
                    "type": "NOTEBOOK",
                    "is_active": 1,
                    "created_by": payload_insert_file['owner'],
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S")
                }
                response_repo_item = table_repo_item.insert(payload_repo_item)
                print("Response Insert Repo Item: {}".format(response_repo_item))



            time.sleep(pollTime)
            if len(fileDiff) == 0: continue
            #doThingsWithNewFiles(fileDiff)
    