def total_occurrences(s1, s2, ch):
    """
    (str, str, str) -> int
    Precondition: len(ch) == 1
    Return the total number of times that ch occurs in s1 and s2.
    >>> total_occurrences('color', 'yellow', 'l')
    3
    >>> total_occurrences('red', 'blue', 'l')
    1
    >>> total_occurrences('green', 'purple', 'b')
    """

    if ch in s1 and ch in s2:
        number = s1.count(ch)
        number1 = s2.count(ch)
        finalnumber = number + number1
        return (print(finalnumber))
    elif ch not in s1 and ch in s2:
        number = s2.count(ch)
        return (print(number))
    else:
        number = int("0")
        return print(number)

total_occurrences('color', 'yellow', 'l')
total_occurrences("green", "red", "l")