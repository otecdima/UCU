import sys
import doctest


def return_digits(number):
    """
    str -> str
    >>> return_digits('123')
    ' 1  222  333 \\n11 2   23   3\\n 1 2  2     3\\n 1   2    33 \\n 1  2       3\\n 1 2    3   3\\n11122222 333 \\n'
    """
    number = str(number)
    row = 0
    result = ""
    while row < 7:
        line = ""
        column = 0
        while column < len(number):
            num = int(number[column])
            digit = Digits[num]
            for i in range(len(digit)):
                digit[i] = digit[i].replace("*", str(num))
            line += digit[row]
            column += 1
        result += line + '\n'
        row += 1
    return print(result)


Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ", "** ", " * ", " * ", " * ", " * ", "***"]
Two = [" *** ", "*   *", "*  * ", "  *  ", " *   ", "*    ", "*****"]
Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ", "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]

try:
    digits = sys.argv[1]
    print(return_digits(digits))
except IndexError:
    print("usage: bigdigits.py <number>")
except ValueError as err:
    print(err, "in", digits)
# print(doctest.testmod())

return_digits('123')