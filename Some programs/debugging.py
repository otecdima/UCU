def sqrt(x:float)-> float:
    """ Return square root of number by Newton's Method
    guess = 1.0

    >>> sqrt(0.023)
    0.15165750888103102

    >>> sqrt(72)
    8.485281374239733
    """

    def sqrt_iter():
        guess = 1.0
        while not good_enough(guess):
            guess = improve(guess)
        return guess

    def improve(guess):
        return average(guess, x/guess)
    
    def average(x, y):
        return (x+y)/2

    def good_enough(guess):
        if round((guess**2), 3) ** 2 == x:
            return 1
        else:
            return 0
    
    return print("Square root of " + str(x) + " =", sqrt_iter())

sqrt(72)


# number = 10
    # spectrum = 10
    # number_list = []
    # for i in range(number):
    #     random_number = random.randrange(spectrum)
    #     number_list.append(random_number)
    # print(number_list)

    # inputcombinations = []
    # # number = int(input(">>> "))
    # # while number != "":
    # #     inputcombinations.append(number)
    # #     number = int(input(">>> ")
    #     # try:
    #     #     number = int(number)
    #     # except:
    #     #     print("Що ти сказав?")

    # print(inputcombinations)
    # for j in range (len(inputcombinations)):
    #     if inputcombinations[j] in number_list and inputcombinations[j] % 2 == 0:
    #         print("Ого, а ти на щось здатен, але не будь таким впевненим, принцеси тобі не бачити!")
    #     if inputcombinations[j] in number_list and inputcombinations[j] % 2 != 0:
    #         print("Ха-ха-ха, неправильно!")