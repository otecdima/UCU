"""Miniproject 1e"""
import argparse

parser = argparse.ArgumentParser(description="That finds the common strings")

parser.add_argument("src1", type=str, help='path to first file')
parser.add_argument("src2", type=str, help='path to second file')
parser.add_argument("dst", type=str, help='path to destination where to save the commons')

args = parser.parse_args()
file_name1 = args.src1
file_name2 = args.src2
new_file1 = args.dst

def files():
    """Finds common strings"""
    try:
        with open(file_name1, "r", encoding = "utf-8") as new_file:
            lst1 = []
            for stringg in new_file:
                stringg = stringg.rstrip()
                lst1.append(stringg)
    except FileNotFoundError:
        print("Incorrect path to first file")
        return
    except IsADirectoryError:
        print("First file is a directory")
        return
    try:
        with open(file_name2, "r", encoding = "utf-8") as new_file:
            lst2 = []
            for stringg in new_file:
                stringg = stringg.rstrip()
                lst2.append(stringg)
    except FileNotFoundError:
        print("Incorrect path to second file")
        return
    except IsADirectoryError:
        print("Second file is a directory")
        return
    new_list = list(set(lst1).intersection(lst2))
    new_list.sort()
    try:
        with open(new_file1, "r", encoding = "utf-8") as file:
            pass
        print("Already exists")
        return
    except IsADirectoryError:
        print("Is a directory")
        return
    except FileNotFoundError:
        pass
    with open(new_file1, "w", encoding='utf-8') as file:
        for element in new_list:
            file.write(element)
            file.write("\n")
files()
