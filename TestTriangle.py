# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testLargeAndSmallInputs(self):
        self.assertEqual(classify_triangle(201, 4, 5), 'InvalidInput')
        self.assertEqual(classify_triangle(4, 201, 5), 'InvalidInput')
        self.assertEqual(classify_triangle(4, 5, 201), 'InvalidInput')
        self.assertEqual(classify_triangle(-1, 5, 8), 'InvalidInput')
        self.assertEqual(classify_triangle(5, -1, 8), 'InvalidInput')
        self.assertEqual(classify_triangle(5, 4, -1), 'InvalidInput')

    def testInvalidInputs(self):
        self.assertEqual(classify_triangle('apple', 3, 4), 'InvalidInput')
        self.assertEqual(classify_triangle(3, 'apple', 4), 'InvalidInput')
        self.assertEqual(classify_triangle(3, 4, 'apple'), 'InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classify_triangle(1, 4, 1), "NotATriangle")
        self.assertEqual(classify_triangle(1, 3, 5), "NotATriangle")
        self.assertEqual(classify_triangle(7, 3, 2), "NotATriangle")

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3, 4, 5),'Right')
        self.assertEqual(classify_triangle(5, 3, 4),'Right')
        self.assertEqual(classify_triangle(4, 5, 3),'Right')

    def testIsoscelesTriangle(self):
        self.assertEqual(classify_triangle(4, 4, 7), 'Isosceles')
        self.assertEqual(classify_triangle(100, 100, 150), 'Isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classify_triangle(3, 5, 7), "Scalene")
        self.assertEqual(classify_triangle(4, 5, 8), "Scalene")
        self.assertEqual(classify_triangle(99, 100, 149), "Scalene")
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1, 1, 1),'Equilateral')
        self.assertEqual(classify_triangle(199, 199, 199),'Equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

