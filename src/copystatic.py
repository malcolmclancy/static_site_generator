import os
import shutil

def copy_files(source_dir_path, dest_dir_path):
    print("Copying static files to {dest_dir_path} directory...")
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    for root, dirs, files in os.walk(source_dir_path):
        dest_dir_path = root.replace(source_dir_path, dest_dir_path)
        for dir in dirs:
            os.mkdir(os.path.join(dest_dir_path, dir))
        for file in files:
            shutil.copy(os.path.join(root, file), dest_dir_path)
