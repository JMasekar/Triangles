"""
@author- Jigar Masekar

HW01 Testing Triangles: Tests for triangle classification

"""

import unittest

from HW01_JM import classify_triangle


class TestTriangles(unittest.TestCase):

    def testRightTriangle(self):
        """ testing right triangles """
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle")
        self.assertEqual(classify_triangle(5, 3, 4), "Right Triangle")

    def testEquilateralTriangle(self):
        """ testing equilateral triangles """
        self.assertEqual(classify_triangle(1, 1, 1), "Equilateral Triangle")
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral Triangle")
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral Triangle")

    def testScaleneTriangle(self):
        """ testing scalene triangles """
        self.assertEqual(classify_triangle(3, 5, 7), "Scalene Triangle")

    def testIsoscelesTriangle(self):
        """ testing isosceles triangles """
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral Triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "Right Triangle")
        self.assertEqual(classify_triangle(3, 4, 3), "Isosceles Triangle")

    def testRandom1(self):
        """ testing invalid values """
        self.assertEqual(classify_triangle(2.5, 5, 8), "Error")
        self.assertEqual(classify_triangle(650, 800, 33), "Error")

    def testRandom2(self):
        """ testing invalid values """
        self.assertEqual(classify_triangle(-5, 8, 12), "Error")
        self.assertEqual(classify_triangle(0, 2, 6), "Error")

    def testRandom3(self):
        """ invalid output testing """
        self.assertNotEqual(classify_triangle(3, 4, 3), "Equilateral Triangle")
        self.assertNotEqual(classify_triangle(3, 3, 6), "Right Triangle")

    def testRandom4(self):
        """ invalid output testing """
        with self.assertRaises(TypeError):
            classify_triangle("a", 3, 5)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
