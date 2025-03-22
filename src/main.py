import os
import shutil
from textnode import TextNode, TextType
from copystatic import copy_files

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory")
    for root, dirs, files in os.walk(dir_path_public):
        for file in files:
            os.remove(os.path.join(root, file))
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

    copy_files(dir_path_static, dir_path_public)

main()