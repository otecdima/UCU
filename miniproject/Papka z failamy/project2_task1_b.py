"""Miniproject 1b"""
import argparse

parser = argparse.ArgumentParser(description="Replaces substring")

parser.add_argument("substring", type=str, help='Substring for changing')
parser.add_argument("substring_to_replace", type=str, help='Substring to replace with')
parser.add_argument("--inplace", action="store_true", help='Rewrites file')
parser.add_argument("filepath", type=str, help='Path to file')

args = parser.parse_args()
substring = args.substring
substring_to_replace = args.substring_to_replace
filepath = args.filepath
inplace = args.inplace

def replace_substring():
    """Rplaces substring"""
    try:
        with open(filepath, "r", encoding = "utf-8") as new_file:
            lst = []
            for stringg in new_file:
                stringg = stringg.rstrip()
                stringg = stringg.replace(substring, substring_to_replace)
                lst.append(stringg)
    except FileNotFoundError:
        print("Incorrect path to first file")
        return

    if not inplace:
        for element in lst:
            print(element)
    else:
        with open(filepath, "w", encoding='utf-8') as file:
            for element in lst:
                file.write(element)
                file.write("\n")
        return file
replace_substring()