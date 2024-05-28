import os
import shutil


class LocalFileManager():
    def __init__() -> None:
        pass

    def move_files(self, source_path, destination_path):
        # copy files from source to destination
        for file in os.listdir(source_path):
            shutil.move(os.path.join(source_path, file), destination_path)