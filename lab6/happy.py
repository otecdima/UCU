"""Function that returns if the ticket number is happy ticket"""
def happy_number(number: int) -> bool:
    """
    >>> happy_number(12345)
    False
    >>> happy_number(43211234)
    True
    >>> happy_number(191234)
    True
    """
    number = (str(number).zfill(8))
    number1 = list(number)
    num1 = number1[:4]
    num1 = [int(i) for i in num1]
    num2 = number1[4:]
    num2 = [int(i) for i in num2]
    for item in num1:
        sumoftheelements1 = sum(num1)
    for item1 in num1:
        sumoftheelements2 = sum(num2)
    if sumoftheelements1 == sumoftheelements2:
        return True
    else:
        return False

"""Returns if the list of happy tickets from the range"""
def happy_numbers(lowernumber: int, uppernumber: int) -> list:
    """
    >>> happy_numbers(10908, 19829)
    [11000]
    """
    happy_numbers_list = []
    lowernumber = int(lowernumber)
    uppernumber = int(uppernumber)
    for _ in range(lowernumber, uppernumber):
        if happy_number(lowernumber):
            happy_numbers_list.append(lowernumber)
        lowernumber = lowernumber + 1
    return happy_numbers_list

"""Returns the number of the happy tickets in the list"""
def count_happy_numbers(n: int) -> int:
    """
    >>> count_happy_numbers(11111)
    5
    """
    return print(len(happy_numbers(0, n)))