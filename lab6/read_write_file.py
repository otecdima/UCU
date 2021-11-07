from typing import List
import re

def read_input_file(url: str, number: int) -> List[List[str]]:
    """
    (str, int) -> (list(list))
    Preconditions: 0 <= number <= 77
    
    Return list of strings lists from url
    
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',1)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80']]
    >>> read_input_file('https://raw.githubusercontent.com/anrom7/Test_Olya/master/New%20folder/total.txt',3)
    [['1', 'Мацюк М. І.', '+', '197.859', '10.80'], ['2', 'Проць О. В.', '+', '197.152', '11.60'], ['3', 'Лесько В. О.', '+', '195.385', '10.60']]
    """
    new_file = urllib.request.urlopen(url)
    new_list = []
    for item in new_file:
        new_list.append(item.decode("utf-8"))

    userdata = []
    some_digit = 0
    for line in data:
        if "#" in line:
            continue
        if some_digit >= number:
            break
        if re.match(pattern ="^[1-9] *", string=line):
            s_s = line.split('\t')
            userdata.append([s_s[0], s_s[1], '+', s_s[3]])
        if re.match(" Середній бал документа про освіту*", line):
            userdata[some_digit].append(line.split(' ')[6].replace("\r\n", ""))
        if re.match("—\t+", line):
            some_digit += 1

    return userdata
    

def write_csv_file(url: str):
     '''
    Creates a csv file
    >>> write_csv_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt')
    '''
    data = read_input_file(url, 1000000)
    lines = ['№,ПІБ,Д,Заг.бал,С.б.док.осв.']
    i = 1
    for item in data:
        item[0] = str(i)
        lines.append(str.join(",", item))
        i += 1

    with open("total.csv", "w", encoding="utf-8") as file:
        file.write("\n".join(lines))

write_csv_file('https://raw.githubusercontent.com/anrom7/\
Test_Olya/master/New%20folder/total.txt')