import unittest
from classify_triangle import classify_triangle
import math


def run_classify_triangle(a, b, c):
    """ invoke classifyTriangle with the specified arguments and print the result """
    print('classifyTriangle(', a, ',', b, ',', c, ') = ', classify_triangle(a, b, c), sep="")


class TestClassifyTriangles(unittest.TestCase):
    def testInvalidTriangles(self):
        self.assertEqual(classify_triangle(1, 2, 4), "Error: Invalid side lengths for triangle.", run_classify_triangle(1, 2, 4))
        self.assertEqual(classify_triangle(4, 2, 1), "Error: Invalid side lengths for triangle.", run_classify_triangle(4, 2, 1))
        self.assertEqual(classify_triangle(2, 4, 1), "Error: Invalid side lengths for triangle.", run_classify_triangle(2, 4, 1))
        self.assertNotEqual(classify_triangle(3, 4, 5), "Error: Invalid side lengths for triangle.", run_classify_triangle(3, 4, 5))
        self.assertNotEqual(classify_triangle(4, 5, 3), "Error: Invalid side lengths for triangle.", run_classify_triangle(4, 5, 3))
        self.assertNotEqual(classify_triangle(5, 3, 4), "Error: Invalid side lengths for triangle.", run_classify_triangle(5, 3, 4))

    def testIncorrectOutputsRight(self):
        self.assertNotEqual(classify_triangle(1, 1, 1), "Equilateral, Right", run_classify_triangle(1, 1, 1))
        self.assertNotEqual(classify_triangle(5, 5, 5), "Equilateral, Right", run_classify_triangle(5, 5, 5))

        self.assertEqual(classify_triangle(3, 4, 5), "Scalene, Right", run_classify_triangle(3, 4, 5))
        self.assertEqual(classify_triangle(10, 6, 8), "Scalene, Right", run_classify_triangle(10, 6, 8))
        self.assertEqual(classify_triangle(12, 20, 16), "Scalene, Right", run_classify_triangle(12, 20, 16))

        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles, Right", run_classify_triangle(1, 1, math.sqrt(2)))
        self.assertEqual(classify_triangle(4 * math.sqrt(2), 4, 4), "Isosceles, Right", run_classify_triangle(4 * math.sqrt(2), 4, 4))
        self.assertEqual(classify_triangle(3, 3 * math.sqrt(2), 3), "Isosceles, Right", run_classify_triangle(3, 3 * math.sqrt(2), 3))

    def testIncorrectOutputNotRight(self):
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral, Not Right", run_classify_triangle(3, 3 * math.sqrt(2), 3))

        self.assertEqual(classify_triangle(3, 5, 6), "Scalene, Not Right", run_classify_triangle(3, 5, 6))
        self.assertEqual(classify_triangle(10, 8, 5), "Scalene, Not Right", run_classify_triangle(10, 8, 5))
        self.assertEqual(classify_triangle(3, 5, 7), "Scalene, Not Right", run_classify_triangle(3, 5, 7))

        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles, Not Right", run_classify_triangle(2, 2, 3))
        self.assertEqual(classify_triangle(5, 3, 3), "Isosceles, Not Right", run_classify_triangle(5, 3, 3))
        self.assertEqual(classify_triangle(7, 13, 7), "Isosceles, Not Right", run_classify_triangle(7, 13, 7))


if __name__ == '__main__':
    unittest.main()
