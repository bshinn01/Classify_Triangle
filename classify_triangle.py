"""
This program contains a function, classify_triangle, which determines whether a triangle
is equilateral, isosceles, or scalene, and whether the triangle is a right triangle
"""

import math


def classify_triangle(a_side, b_side, c_side):
    """
    This function classifies triangles as equilateral, isosceles, and scalene, as well as
    whether the triangle is a right triangle based on the side length params

    :param a_side: side length of triangle
    :param b_side: side length of triangle
    :param c_side: side length of triangle
    :return: 'Equilateral', 'Isosceles', or 'Scalene', and 'Right' or 'Not Right'
    """
    longest_side = max(a_side, b_side, c_side)
    other_sides = [a_side, b_side, c_side]
    other_sides.remove(longest_side)
    if (a_side + b_side <= c_side) or (a_side + c_side <= b_side) or (c_side + b_side <= a_side):
        return "Error: Invalid side lengths for triangle."
    if int(math.pow(longest_side, 2)) == math.pow(other_sides[0], 2) + \
            math.pow(other_sides[1], 2):
        if (a_side != b_side) and (b_side != c_side) and (a_side != c_side):
            return "Scalene, Right"
        return "Isosceles, Right"
    if (a_side == b_side) and (b_side == c_side):
        return "Equilateral, Not Right"
    if (a_side != b_side) and (b_side != c_side) and (a_side != c_side):
        return "Scalene, Not Right"
    return "Isosceles, Not Right"
