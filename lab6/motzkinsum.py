def motzkin_sum_numbers(length):
    """
    >>> motzkin_sum_numbers(15)
    [1, 0, 1, 1, 3, 6, 15, 36, 91, 232, 603, 1585, 4213, 11298, 30537]
    """
    new_list = []
    len = list(range(1, length))
    new_list.append(1)
    for i in len:
        # element_in_list = bin(i)
        element_in_list = int((i-1)*(2 * new_list[i-1] + 3 * new_list[i-2])/(i+1))
        new_list.append(element_in_list)
    # return new_list

print(motzkin_sum_numbers(15))