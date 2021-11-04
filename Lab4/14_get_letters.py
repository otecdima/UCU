def get_letters(n):
    """
    int -> str
    Create and return string of first n letters of an alphabet. If arguments isn't
    positive integer number function should return None.

    >>> get_letters(0)

    >>> get_letters(1)
    a
    >>> get_letters(-2015)

    """
    if n > 0:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        new_string= alphabet[0:n]
        return print(new_string)
    elif n == 0 or n <= 0:
        return None

get_letters(0)
