def polygon_area(vertices):
    """
    >>> polygon_area([(4,10), (9,7), (11,2), (2,2)])
    45.5
    >>> polygon_area([(9,7), (11,2), (2,2), (4, 10)])
    45.5
    >>> polygon_area([(0, 0), (0.5,1), (1,0)])
    0.5
    >>> polygon_area([(0, 10), (0.5,11), (1,10)])
    0.5
    >>> polygon_area([(-0.5, 10), (0,-11), (0.5,10)])
    10.5

    """
    len_of_vertices = len(vertices)
    newarea = 0
    for item in range(len_of_vertices):
        if item + 1 != len_of_vertices:
            semiarea = (vertices[item][0] * vertices[item + 1][1] - vertices[item + 1][0] * vertices[item][1])
        else:
            semiarea =  vertices[item][0] * vertices[0][1] - vertices[0][0] * vertices[item][1]
        newarea = newarea + semiarea
    newarea = abs(newarea)
    finalarea = 0.5 * newarea
    return finalarea

print(polygon_area([(4,10), (9,7), (11,2), (2,2)]))
print(polygon_area([(9,7), (11,2), (2,2), (4, 10)]))
print(polygon_area([(0, 0), (0.5,1), (1,0)]))
print(polygon_area([(0, 10), (0.5,11), (1,10)]))
print(polygon_area([(-0.5, 10), (0,-11), (0.5,10)]))