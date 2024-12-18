import os
from shutil import move

def organize_folder(folder_path):
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            ext = file.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            move(os.path.join(folder_path, file), os.path.join(ext_folder, file))

# Example usage
organize_folder("C:/Users/YourName/Downloads")