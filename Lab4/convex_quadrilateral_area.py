from math import sqrt


def four_lines_area(koef1, c1, koef2, c2,
    koef3, c3, koef4, c4):
    """Return rounded quadrangle area
    """
    x1, y1 = lines_intersection(koef1, c1, koef2, c2)
    x2, y2 = lines_intersection(koef2, c2, koef3, c3)
    x3, y3 = lines_intersection(koef3, c3, koef4, c4)
    x4, y4 = lines_intersection(koef4, c4, koef1, c1)

    side_ab = distance(x1, y1, x2, y2)
    side_bc = distance(x2, y2, x3, y3)
    side_cd = distance(x3, y3, x4, y4)
    side_ad = distance(x4, y4, x1, y1)

    diagonal1 = distance(x1, y1, x3, y3)
    diagonal2 = distance(x2, y2, x4, y4)

    area_of_quadrangle = quadrangle_area(side_ab, side_bc, side_cd,
    side_ad, diagonal1, diagonal2)

    return round(area_of_quadrangle, 2)


def lines_intersection(koef1, c1, koef2, c2):
    """Returns the intersections of the lines
    """
    if koef1 == koef2:
        return None

    x_intersection_for_two_lines = (c2 - c1)/(koef1 - koef2)
    y_intersection_for_two_lines = koef1 * x_intersection_for_two_lines + c1
    x_intersection_for_two_lines = round(x_intersection_for_two_lines, 2)
    y_intersection_for_two_lines = round(y_intersection_for_two_lines, 2)
    return x_intersection_for_two_lines, y_intersection_for_two_lines


def distance(x1, y1, x2, y2):
    """Returns te distance between two points
    """
    theside = sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(theside, 2)


def quadrangle_area(side_ab, side_bc, side_cd, side_ad, diagonal1, diagonal2):
    """Returns the area of quadrangle
    """
    if (4 * (diagonal1 ** 2) * (diagonal2 ** 2)) < ((side_bc ** 2 +
       side_ad ** 2 - side_ab ** 2 - side_cd ** 2) ** 2):
        return None
    if side_ab <= 0 or side_bc <= 0 \
       or side_cd <= 0 or side_ad <= 0 \
       or diagonal1 <= 0:
        return None
    S = sqrt((4 * (diagonal1 ** 2) * (diagonal2 ** 2) - \
    (side_bc ** 2 + side_ad ** 2 - side_ab ** 2 - side_cd ** 2) ** 2)/16)
    return round(S, 2)

