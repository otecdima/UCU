# def get_root(function, param_a, param_b):
#     """
#     (function or str, number, number) -> (number)
#     Compute and return root of the function f in the interval (a, b).
#     >>> get_root('x', -1, 1)
#     0.0
#     >>> get_root(lambda x: x, -1, 1)
#     0.0
#     """
    
#     res = float(param_a)
#     if isinstance(function, str):
#         function = eval("lambda x: " + function) 
#     if function(param_a) < 0:
#         while not function(res) == 0:
#             res = (param_a + param_b) / 2
#             if function(res) > 0:
#                 param_b = res
#             elif function(res) <0:
#                 param_a = res
#     elif function(param_b) < 0:
#         while not function(res) == 0:
#             res = (param_a + param_b) / 2
#             if function(res) <0:
#                 param_b = res
#             elif function(res) > 0:
#                 param_a = res
#     return round(res, 2)


def get_root(func, frst_x, sec_x):
    """
    (function or str, number, number) -> (number)

    Compute and return root of the function f in the interval (a, b).

    >>> get_root('x', -1, 1)
    0.0
    >>> get_root(lambda x: x+1.25, -2, 2)
    -1.25
    """
    if isinstance(func, str):
        func = eval('lambda x: ' + func)
    # if sec_x > 0:
    #     uper = sec_x
    # else:
    #     uper = frst_x
        
    # if frst_x <= 0:
    #     lower = frst_x
    # else:
    #     lower = sec_x
    new_mid = (frst_x+sec_x)/2
    res = func(new_mid)
    res = round(res, 2)
    for _ in range(10):
        if res == 0:
            new_mid = round(new_mid, 2)
            return new_mid
        if res < 0:
            frst_x = new_mid
        else:
            sec_x = new_mid
        new_mid = (frst_x+sec_x)/2
        
# print(get_root('x', -1, 1))
print(get_root('x ** 2 - 7', -2, 3))
# print(get_root(lambda x: x, -1, 1))

















# f = "x ** 2 + x"
# mass = [1, 2, 3, -1, 3]
# f = eval('lambda x: ' + f)
# nre_list = []
# finallist = []
# for item in mass:
#     everyvalue = f(item)
#     nre_list.append(everyvalue)
# maxx = max(nre_list)
# for item1 in mass:
#     if f(item1) == maxx:
#         finallist.append(item1)

# print(finallist)