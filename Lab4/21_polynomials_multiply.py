def polynomials_multiply(polynom1, polynom2):
    """
    # (2x)*(3x) == 6
    >>> polynomials_multiply([2], [3])
    [6]
    # (2x-4)*(3x+5) == 6x^2 -2x - 20
    >>> polynomials_multiply([2,-4],[3,5])
    [6,-2,-20]
    # (2x^2-4)*(3x^3+2x) == (6x^5-8x^3-8x)
    >>> polynomials_multiply([2,0,-4],[3,0,2,0])
    [6,0,-8,0,-8,0]

    """

    # polynom1.reverse()
    # polynom2.reverse()
#     polynom_length = len (polynom1) + len(polynom2) - 1
#     res = [0] * polynom_length
#     ln1 = len(polynom1)
#     ln2 = len(polynom2)
#     for i in range(ln1):
#         for j in range(ln2):
#             res[i+j] += polynom1[i]*polynom2[j]
#     # res.reverse()
#     return res
# # print(polynomials_multiply([2], [3]))
# print(polynomials_multiply([2,-4],[3,5]))


    len_of_first = len(polynom1)
    len_of_second = len(polynom2)
    result = [0] * (len_of_first + len_of_second - 1)
    for item in range(len_of_first):
        for jtem in range(len_of_second):
            result[item + jtem] = result[item + jtem] + polynom1[item]*polynom2[jtem]
    return result

print(polynomials_multiply([2], [3]))
    
print(polynomials_multiply([2,-4],[3,5]))
    
print(polynomials_multiply([2,0,-4],[3,0,2,0]))

# if __name__ == "__main__":
#     import doctest
#     print(doctest.testmod())