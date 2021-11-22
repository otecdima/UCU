""" MY LAB TASK """

import argparse
import os

def prsr_crea():
    """Creates parser"""
    parser = argparse.ArgumentParser(description='Deleting a phrase from a file')
    # parser.add_argument('--offset', type=int, nargs='?', default=13, const=13, help='zsuv')
    # parser.add_argument('--decrypt',
    # action='store_true', help="""File that will be found and procesed""")
    # parser.add_argument('--inplace', action='store_true', help="""If that is done,
    # file will be changed""")
    parser.add_argument('src', type=str, help='first file')
    # parser.add_argument('src2', type=str, help='second file')
    parser.add_argument('dst', type=str, help='that, that is different in both files')
    return parser.parse_args()

def for_file(path, new_dir, cur_dir, file):
    # for i in [path, new_dir, cur_dir, file]:
    #     print(i)
    print(file)
    # try:
    #     os.mkdir(path.replace(file, '').replace(cur_dir, new_dir))
    # except FileExistsError:
    #     pass
    # except Exception as er:
    #     print(er)
    old_fl = open(path, 'r')
    new_fl = open(path.replace(cur_dir, new_dir), 'w')
    new_fl.write(old_fl.read())
    old_fl.close()
    new_fl.close()

def fr_dir(path, new_dir, cur_dir):
    os.chdir(path)
    try:
        os.mkdir(path.replace(cur_dir, new_dir))
    except FileExistsError:
        pass
    except Exception as er:
        print(er)
    for elem in os.listdir():
        path = os.path.join(os.getcwd(), elem)
        if os.path.isfile(path):
            for_file(path, new_dir, cur_dir, elem)
        elif os.path.isdir(path):
            fr_dir(path, new_dir, cur_dir)

def changer(args):
    cur_dir = args.src
    new_dir = args.dst
    os.chdir(cur_dir)
    print(os.listdir())
    for elem in os.listdir():
        os.chdir(cur_dir)
        path = os.path.join(os.getcwd(), elem)
        print(path, os.path.isfile(path), os.path.isdir(path))
        if os.path.isfile(path):
            print("I'm file", path)
            for_file(path, new_dir, cur_dir, elem)
        elif os.path.isdir(path):
            print("I'm folder", path)
            fr_dir(path, new_dir, cur_dir)


if __name__ == '__main__':
    args = prsr_crea()
    print('====================')
    try:
        os.mkdir(args.dst)
        print(args.src)
        os.chdir(args.src)
    except FileExistsError:
        pass
    except FileNotFoundError:
        print('There is no such file')
    except Exception as ex:
        print('nesto drugo', ex)
    changer(args)

# x = '/home/josipjelacic/python_linux/temp'
# y = '/home/josipjelacic/python_linux/sec_temp'

