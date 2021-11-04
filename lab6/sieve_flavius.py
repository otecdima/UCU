from typing import List

def sieve_flavius(elements_number: int) -> List[int]:
    list_of_numbers = []
    for i in range(1, elements_number):
        list_of_numbers.append(i)
    for item in list_of_numbers:
        if item % 2 == 0:
            list_of_numbers.remove(item)
    variable = 1
    while variable < len(list_of_numbers): 
        del list_of_numbers[list_of_numbers[variable]-1::list_of_numbers[variable]]
        variable = variable + 1
    return print(list_of_numbers)   

sieve_flavius(1)