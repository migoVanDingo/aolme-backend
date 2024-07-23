import os
import subprocess

from flask import current_app

class GitUtility:
    def __init__(self)->None:
        pass

    def git_init(self, path:str)->str:
        try:
            
            os.chdir(path)
            subprocess.run(['git', 'init'])
            subprocess.run(['dvc', 'init'])
            return "success"
        except Exception as e:
            return str(e)
        

    def clone(self, url: str, repo_id: str, entity_id: str) -> str:
        try:
        
            os.chdir(os.path.join(os.environ["REPO_DIRECTORY"],repo_id, "project"))
            subprocess.run(['git', 'clone', url])
            current_app.logger.debug(f"{self.__class__.__name__} :: Cloning repository :: url: {url} :: repo_id: {repo_id} :: entity_id: {entity_id}")

            dir = os.listdir(os.path.join(os.environ["REPO_DIRECTORY"],repo_id, "project"))

            return dir[0]
        except Exception as e:
            return str(e)
        
    def sync_repo(self, repo_id: str, dir_name: str) -> None:
        try:
            os.chdir(os.path.join(os.environ["REPO_DIRECTORY"],repo_id, "project", dir_name))
            subprocess.run(['git', 'fetch'])
            subprocess.run(['git', 'pull'])
            current_app.logger.debug(f"{self.__class__.__name__} :: Syncing repository :: repo_id: {repo_id}")

            return "REPO_SYNCED"
        except Exception as e:
            return str(e)
