"""[sumary]
"""
def digit_sum(num: int) -> int:
    """Retturn sum of number digits
    :param num: [description] 
    type num: int
    """
    def add_digits(num):


        total = 0
        while num > 0:
            num, rem = divmod(num, 10)
            total += rem
        return total
    

    if num == 0:
        return 0

    total = add_digits(num)
    while total > 9:
        total = add_digits(total)
    return total


    
# print(digit_sum(3456))

# if __name__ == '__main__':
#     import doctest
#     print(doctest.testmod())