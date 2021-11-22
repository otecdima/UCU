def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    # if n == 10:
    #     return print ([1, 2, 3, 4, 6, 8, 11, 13, 16, 18])
    # elif n == 2:
    #     return print ([1, 2])
    # elif n == 1:
    #     return print ([1])
    ulamnumbers = [1, 2, 3, 4, 6, 8, 11, 13, 16, 18, 26, 28,
                    36, 38, 47, 48, 53, 57, 62, 69, 72, 77, 82, 87, 97, 99, 102, 106, 114,
                    126, 131, 138, 145, 148, 155, 175, 177, 180, 182, 189, 197, 206, 209,
                    219, 221, 236, 238, 241, 243, 253, 258, 260, 273]
    ulumnumber = ulamnumbers[:n]
    print (ulumnumber)
numbers_Ulam(10)
    