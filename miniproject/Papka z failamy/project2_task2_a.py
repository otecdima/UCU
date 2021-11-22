"""Miniproject 2a"""
import os
import argparse

parser = argparse.ArgumentParser(description="Build the tree of files and directories")

parser.add_argument("startwith", type=str, help='directoru to start with')

args = parser.parse_args()
startwith = args.startwith

def list_files():
    try:
        for root, _, files in os.walk(startwith):
            level_of_dir = root.replace(startwith, '').count(os.sep)
            print("│  " * level_of_dir, "├───── ", os.path.basename(root), "/", sep="")
            for item in range(len(files)):
                print('│  ' * (level_of_dir + 1), "├───── ", files[item], sep="")
            if item + 1 == len(files):
                print('│  ' * (level_of_dir + 1), "└──", files[item], sep="")
    except:
        print("Your path is incorent")
list_files()