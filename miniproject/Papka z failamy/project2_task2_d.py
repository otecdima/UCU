"""Copy tree"""
import os
import argparse
parser = argparse.ArgumentParser(description="Copy tree")

parser.add_argument("src", type=str, help="path to first directory")
parser.add_argument("dst", type=str, help='path to second directory')

args = parser.parse_args()
src1 = args.src
dst1 = args.dst

if not os.path.exists(dst1):
    os.makedirs(dst1)
    
def for_file(path, new_dir, cur_dir, file):
    print(file)
    with open(path, 'r', encoding = 'utf-8') as old_fl:
        with open (path.replace(cur_dir, new_dir), 'w', encoding = 'utf-8') as new_fl:
            new_fl.write(old_fl.read())

def function():
    os.chdir(src1)
    for elem in os.listdir():
        path = os.path.join(os.getcwd(), elem)
        if os.path.isfile(path):
            for_file(path, dst1, src1, elem)
function()