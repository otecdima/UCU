def replace_with_stars(s):
    """
    str -> str
    Replace symbols in string with stars. If argument is not a string function should
    return None.

    >>> number_of_sentences("Revenge is a dish that tastes best when served cold.")
    ****************************************************
    >>> number_of_sentences("Never hate your enemies. It affects your judgment.")
    **************************************************
    >>> number_of_sentences(2015)

    """
    if type(s) == str:
        replaced = s
        for character in replaced:
            s = s.replace(character, "*")
        return s
    else:
        return None

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
