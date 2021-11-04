def number_of_capital_letters(s):
    """
    str -> str
    Find and return number of capital letters in string. If argument isn't string
    function should return None.

    >>> number_of_capital_letters("ArithmeticError")
    2
    >>> number_of_occurence("EOFError")
    4
    >>> number_of_capital_letters(1)

    """
    if type(s) == str:
        count = 0
        for item in s:
            if item.isupper():
                count += 1
        return print(count)
    else:
        return None

number_of_capital_letters(7)
