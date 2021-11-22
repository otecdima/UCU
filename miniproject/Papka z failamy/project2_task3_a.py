import zipfile
import os
import re
import argparse

parser = argparse.ArgumentParser(description="Find in the archive all files that contain a regular \
    expression, remove (copy) from the original archive and create \
    a separate archive with these files. The original archive should remain as it was.")

parser.add_argument("regularexpression", type=str, help='regular expression')
parser.add_argument("path_to_archive", type=str, help='path to archive')
parser.add_argument("path_where_to_save_archive", type=str, help='path where to save archive')

args = parser.parse_args()
regular_expression = args.regularexpression
path_to_archive = args.path_to_archive
path_where_to_save_archive = args.path_where_to_save_archive

def zipwithregular():
    """finds regular expressions in the archive and move it to another archive"""
    list_of_files = []
    new_list = []
    try:
        with zipfile.ZipFile(path_to_archive, "r" ) as my_zip1: 
            my_zip1.extractall("directory")
    except FileNotFoundError:
        print("The zip file you want to open doesn't exist or path is incorect")
        return 
    except PermissionError:
        print("The zip you want to open is directory")
        return
    for _, _, files in os.walk("directory"):
        for item in files:
            list_of_files.append(item)
    for element in list_of_files:
        find = re.search(regular_expression, str(element))
        if find:
            new_list.append(element)

    with zipfile.ZipFile(path_where_to_save_archive, "w") as zip_file:
        for element in new_list:
            zip_file.write(element)

    dir = 'directory'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    os.rmdir("directory")
zipwithregular()