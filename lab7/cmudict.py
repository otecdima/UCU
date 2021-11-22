"""Lab 7.3"""
def dict_reader_tuple(file_dict):
    '''
    Returns a tuple of the file opened
    >>> dict_reader_tuple("c1.txt") #doctest: +ELLIPSIS
    [('A', 1, ['AH0']), ('A.', 1, ['EY1']),...
    '''
    with open(file_dict, 'r', encoding = 'utf-8') as new_file:
        the_dictionary = []
        for everyline in new_file:
            everyline = everyline.rstrip()
            everyline.split()
            word = everyline.split(" ")[0]
            number = int(everyline.split(" ")[1])
            othersymbols = everyline.split(" ")[2:]
            new_tuple = (word, number, othersymbols)
            the_dictionary.append(new_tuple)
        return the_dictionary

def dict_reader_dict(file_dict):
    '''
    Returns a dictinary of elements from a file
    >>> dict_reader_dict("c1.txt") #doctest: +ELLIPSIS
    {...
    '''
    with open(file_dict, 'r', encoding = 'utf-8') as new_file:
        listt = []
        newwdict = {}
        for everyline in new_file:
            everyline = everyline.rstrip()
            everyline.split()
            word = everyline.split(" ")[0]
            number = int(everyline.split(" ")[1])
            othersymbols = everyline.split(" ")[2:]
            new_tuple = (word, number, othersymbols)
            listt.append(new_tuple)
        for item in listt:
            if item[0] not in newwdict:
                pronunciationletters = set()
                othersymbols1 = tuple(item[2])
                pronunciationletters.add(othersymbols1)
                newwdict.setdefault(item[0], pronunciationletters)
            elif item[0] in newwdict:
                othersymbols12 = tuple(item[2])
                newwdict[item[0]].add(othersymbols12)
        return newwdict

def dict_invert(dct):
    '''
    Inverts the dict
    >>> dict_invert(dict_reader_tuple('c1.txt')) #doctest: +ELLIPSIS
    {1: {('...
    '''
    if isinstance(dct, list):
        dictinary = {}
        for word in dct:
            if word[0] in dictinary:
                dictinary[word[0]].add(tuple(word[2]))
            else:
                tempor_set = set()
                tempor_set.add(tuple(word[2]))
                dictinary[word[0]] = tempor_set
        dct = dictinary
    return_dictinary = {}
    for key in dct:
        letters = list(dct[key])
        len_letters = len(letters)
        if len_letters in return_dictinary:
            letters_set = set()
            for i in range(len_letters):
                val_of_key = tuple((key, letters[i]))
                letters_set.add(val_of_key)
            return_dictinary[len_letters].update(letters_set)
        else:
            letters_set = set()
            for i in range(len_letters):
                val_of_key = tuple((key, letters[i]))
                letters_set.add(val_of_key)
            return_dictinary.setdefault(len_letters, letters_set)

    return dict(sorted(return_dictinary.items(), key=lambda x: x[0]))
print(dict_invert(dict_reader_tuple('cmudict.txt')))