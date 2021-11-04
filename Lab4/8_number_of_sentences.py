import re

def number_of_sentences(s):
    """
    str -> str
    Return number of sentence in the string. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    1
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    2
    >>> number_of_sentences(2015)

    """

    if type (s) == str:
        count = len(re.findall(r'\.', s))
        return print(count)
    else:
        return None

number_of_sentences(45)
