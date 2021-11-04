def pascal_triangle(n):
    """
    Returns the pascal's triangle
    >>> pascal_triangle(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    >>> pascal_triangle(1)
    [[1], [1, 1]]
    >>> pascal_triangle(-1)
    []
    """
    if n > 0:
        triangle_rows = [[1]]
        for i in range(1, n):
            middle_numbers_list = []
            for pair in zip(triangle_rows[-1], triangle_rows[-1][1:]):
                middle_numbers_list.append(sum(pair))
            triangle_rows.append([1] + middle_numbers_list + [1])
        return print(triangle_rows)
    else:
        return print([])
pascal_triangle(5)
pascal_triangle(0)

