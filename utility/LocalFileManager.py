import os
import shutil


class LocalFileManager():
    def __init__(self) -> None:
        pass

    def move_files(self, source_path, destination_path):
        # copy files from source to destination
        for file in os.listdir(source_path):
            shutil.move(os.path.join(source_path, file), destination_path)

    def get_directory_content(self, path):
        raw_content = os.listdir(path)
        content = []
        for item in raw_content:
            if os.path.isdir(os.path.join(path, item)):
                content.append({"item": item, "is_dir": True})
            else:
                content.append({"item": item, "is_dir": False})

        return content