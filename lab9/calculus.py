"""LAB 9.2"""
def find_max_1(function, points):
    """
    (function or str, list(number)) -> (number)
    Find and return maximal value of function f in points.
    >>> find_max_1('x ** 2 + x', [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    """
    if isinstance (function, str):
        function = eval('lambda x: ' + function)
    new_list = []
    for item in points:
        everyvalue = function(item)
        new_list.append(everyvalue)
    maxvalue = max(new_list)
    return maxvalue

def find_max_2(function, newpoints):
    """
    (function or str, list(number)) -> (number)
    Find and return list of points where function f has the maximal value.
    >>> find_max_2('x ** 2 + x', [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    """
    if isinstance (function, str):
        function = eval('lambda x: ' + function)
    new_list = []
    finallist = []
    for item in newpoints:
        everyvalue = function(item)
        new_list.append(everyvalue)
    maxx = max(new_list)
    for jtem in newpoints:
        if function(jtem) == maxx:
            finallist.append(jtem)
    return finallist

def compute_limit(sequence):
    """
    (function or str) -> (number)
    Compute and return limit of a convergent sequence.
    >>> compute_limit('(n ** 2 + n) / n ** 2')
    1.0
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    """
    lst = []
    if isinstance(sequence, str):
        sequence = eval('lambda n: ' + sequence)
    i = 0
    while True:
        value = sequence(10 ** i)
        lst.append(value)
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            limit_of_sequence = round(lst[i], 2)
            break
        i += 1
    return limit_of_sequence

def compute_derivative(function, x_0):
    """
    (function or str, number) -> (number)
    Compute and return derivative of function f in the point x_0.
    >>> compute_derivative('x ** 2 + x', 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    """
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    aprox = []
    i = 0
    while True:
        diferentialx =  10 ** -i
        xvariable = x_0 + diferentialx
        diferentialf = function(xvariable)
        xvariable = x_0
        diferentialf -= function(xvariable)
        der = diferentialf / diferentialx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            deriviate = round(aprox[i], 2)
            break
        i += 1
    return deriviate

def get_tangent(function, x_0):
    """
    (function or str, number) -> (str)
    Compute and return tangent line to function f in the point x_0.
    >>> get_tangent('x ** 2 + x', 2)
    '5.0 * x - 4.0'
    >>> get_tangent('- x ** 2 + x', 2)
    '- 3.0 * x + 4.0'
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    aprox = []
    i = 0
    while True:
        diferentialx =  10 ** -i
        xvariable = x_0 + diferentialx
        diferentialf = function(xvariable)
        xvariable = x_0
        diferentialf -= function(xvariable)
        der = diferentialf / diferentialx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            deriviate = round(aprox[i], 2)
            break
        i += 1
    resultstrig = ""
    if deriviate > 0 and (deriviate * (-x_0)) < 0:
        resultstrig += str(abs(deriviate)) + " * x " + "- " + \
        str(abs(deriviate * (-x_0) + function(x_0)))
    if deriviate > 0 and ((deriviate * (-x_0))) > 0:
        resultstrig += str(abs(deriviate)) + " * x " + "+ " + \
            str(abs(deriviate * (-x_0) + function(x_0)))
    if deriviate < 0 and (deriviate * (-x_0)) < 0:
        resultstrig += "- " + str(abs(deriviate)) + " * x " + "- " + \
            str(abs(deriviate * (-x_0) + function(x_0)))
    if deriviate < 0 and (deriviate * (-x_0)) > 0:
        resultstrig += "- " + str(abs(deriviate)) + " * x " + "+ " + \
            str(abs(deriviate * (-x_0) + function(x_0)))
    return resultstrig

def get_root(function, arg1, arg2):
    """
    (function or str, number, number) -> (number)
    Compute and return root of the function f in the interval (a, b).
    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    if isinstance(function, str):
        function = eval('lambda x: ' + function)
    # for item in range(arg1 * 1000, arg2 * 1000):
    #     rounds = round(function(item / 1000), 2)
    #     if rounds == 0:
    #         value_of_fuction = round((item / 1000), 2)
    # return value_of_fuction
# print(get_root('x ** 2 - 7', -1, 1))

    newargument = arg1
    while arg2 > newargument:
        rounds = round(function(newargument), 2)
        if rounds == 0:
            value_of_fuction = round(newargument, 2)
        newargument = newargument + 0.001
    return value_of_fuction
            


