import math


def classify_triangle(a, b, c):
    """
    This function classifies triangles as equilateral, isosceles, and scalene, as well as
    whether or not the triangle is a right triangle based on the side length params

    :param a: side length of triangle
    :param b: side length of triangle
    :param c: side length of triangle
    :return: 'Equilateral', 'Isosceles', or 'Scalene', and 'Right' or 'Not Right'
    """
    longest_side = max(a, b, c)
    other_sides = [a, b, c]
    other_sides.remove(longest_side)
    if (a + b <= c) or (a + c <= b) or (c + b <= a):
        return "Error: Invalid side lengths for triangle."
    elif int(math.pow(longest_side, 2)) == math.pow(other_sides[0], 2) + math.pow(other_sides[1], 2):
        if (a == b) and (b == c):
            return "Equilateral, Right"
        elif (a != b) and (b != c) and (a != c):
            return "Scalene, Right"
        else:
            return "Isosceles, Right"
    elif (a == b) and (b == c):
        return "Equilateral, Not Right"
    elif (a != b) and (b != c) and (a != c):
        return "Scalene, Not Right"
    else:
        return "Isosceles, Not Right"
