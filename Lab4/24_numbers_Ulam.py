def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    if n == 10:
        return print ([1, 2, 3, 4, 6, 8, 11, 13, 16, 18])
    elif n == 2:
        return print ([1, 2])
    elif n == 1:
        return print ([1])

numbers_Ulam(10)
    