def create_string(lst):
    """
    list -> str
    Create and return string from histogrma of letters. If argument isn't list of 26 positive
    integer numbers function should return None.

    >>> create_string([0, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    bcc
    >>> create_string([4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4])
    aaaazzzz
    >>> create_string([4, 0, 0, 0, 0, 0])

    """
    lenoftheletters = len(lst)
    if lenoftheletters != 26:
        return None
    new_string = ""
    for item in range(lenoftheletters):
        if lenoftheletters[item] != 0:
            letter = chr(item + 97) * lenoftheletters[item]
            new_string = new_string + letter
    return new_string
    