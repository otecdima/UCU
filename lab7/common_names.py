"""Lab 7,2"""
def names_read(file_name):
    '''
    This function returns a list of names from files
    >>> names_read('female.txt') #doctest: +ELLIPSIS
    {...
    '''
    with open(file_name, "r", encoding = "utf-8") as new_file:
        list_of_names = [string.rstrip() for string in new_file]
    return set(list_of_names)
# print(names_read('female.txt'), names_read('male.txt'))

def common_names(female_names, male_names):
    '''
    Retrun common names from two sets
    >>> common_names(names_read('male.txt'), \
names_read('female.txt'))  #doctest: +ELLIPSIS
    {...
    '''
    vowels = ['A', 'E', 'I', 'O', 'U']
    new_list = []
    female_names = set(female_names)
    male_names = set(male_names)
    common_names1 = female_names & male_names
    for item in common_names1:
        if item[0] in vowels:
            new_list.append(item)
    return set(new_list)

print(common_names(names_read('female.txt'), names_read('male.txt')))
