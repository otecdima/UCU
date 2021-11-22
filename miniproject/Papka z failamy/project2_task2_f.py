"""Miniproject 2f"""
import os
import re
import argparse

parser = argparse.ArgumentParser(description="Program for finding regular expressions")

parser.add_argument("expression", type=str, help='Regular expression')
parser.add_argument("newexpression", type=str, help='New regular expression')
parser.add_argument("--show_lines", action="store_true", help='to show lines')
parser.add_argument("--only_show_counts", action="store_true", help='to show only matches')

args = parser.parse_args()
expression = args.expression
newexpression = args.newexpression
showlines = args.show_lines
onlycounts = args.only_show_counts
if args.only_show_counts and args.show_lines:
    print("Choose only one argument")

def grep():
    """
    Analogue of grep
    """
    directory1 = os.getcwd()
    for root, _, files in os.walk(directory1):
        for element in files:
            find = re.search(expression, element)
            if find:
                os.chdir(root)
                with open(element, "r", encoding = "utf-8") as new_file:
                    counts = 1
                    counts1 = 0
                    fnding = False
                    for stringg in new_file:
                        stringg = stringg.rstrip()
                        newfind = re.search(newexpression, stringg)
                        if newfind:
                            counts1+=1
                            if not fnding:
                                print('\n', element, sep='')
                                fnding = True
                            if showlines:
                                print(counts, ":", stringg.strip('\n'))
                            if not showlines and not onlycounts:
                                print(stringg.strip('\n'))
                        counts = counts + 1
                    if onlycounts:
                        print(counts1)
grep()
