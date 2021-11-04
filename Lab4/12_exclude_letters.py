def exclude_letters(s1, s2):
    """
    (str, str) -> str
    Delete all letter from string s2 in string s1. If arguments aren't strings function should
    return None.

    >>> exclude_letters("aaabb", "b")
    aaa
    >>> exclude_letters("abcc", "cczzyy")
    ab
    >>> exclude_letters(2015, "sasd")

    """
    if type (s1) == str and type(s2) == str:
        replaced = s2
        for character in replaced:
            s1 = s1.replace(character, "")
        return print(s1)
    else:
        return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
    