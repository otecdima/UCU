"""Miniproject 3e"""
import zipfile
import os
import argparse

parser = argparse.ArgumentParser(description="Connect the contents of two archives itno one")

parser.add_argument("src1", type=str, help='path to first archive')
parser.add_argument("src2", type=str, help='path to second archive')
parser.add_argument("dst", type=str, help='path to setination archive')

args = parser.parse_args()
zipfile1 = args.src1
zipfile2 = args.src2
new_zip = args.dst

try:
    name1 = os.path.basename(zipfile1)
    zipfile1 = zipfile.ZipFile(name1, 'r')
    list_of_files1 = zipfile1.namelist()
    zipfile1.close()
except FileNotFoundError:
    print("The zip file you want to open doesn't exist or path is incorect")
except PermissionError:
    print("The zip you want to open is directory")
try:
    name2 = os.path.basename(zipfile2)
    zipfile2 = zipfile.ZipFile(name2, 'r')
    list_of_files2 = zipfile2.namelist()
    zipfile1.close()
except FileNotFoundError:
    print("The zip file you want to open doesn't exist or path is incorect")
except PermissionError:
    print("The zip you want to open is directory")

newzipfile = zipfile.ZipFile(new_zip, 'w')
for file in list_of_files1:
    newzipfile.write(file)
for files in list_of_files2:
    newzipfile.write(files)
zipfile1.close()