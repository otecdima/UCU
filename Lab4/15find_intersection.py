def find_intersection(s1, s2):
    """
    (str, str) -> str
    Find and returs string of all letters in alphabetic order that
    are present in both strings. If arguments aren't strings function
    should return None.

    >>> find_intersection("aaabb", "bbbbccc")
    b
    >>> find_intersection("aZAbc", "zzYYxp")
    z
    >>> find_intersection("sfdfsdf", 2015)

    """
    if type(s1) == str and type(s2) == str:
        for item in s1 and s2:
            if item in s1 and s2:
                return print(item)
            elif (item.isupper() and item in s1) or (item.islower() and item in s2):
                return print(item.lower())
    else:
        return None
find_intersection("aaabb", "bbbbccc")