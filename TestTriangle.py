# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testLargeAndSmallInputs(self):
        self.assertEqual(classifyTriangle(201, 4, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(4, 201, 5), 'InvalidInput')
        self.assertEqual(classifyTriangle(4, 5, 201), 'InvalidInput')
        self.assertEqual(classifyTriangle(-1, 5, 8), 'InvalidInput')
        self.assertEqual(classifyTriangle(5, -1, 8), 'InvalidInput')
        self.assertEqual(classifyTriangle(5, 4, -1), 'InvalidInput')

    def testInvalidInputs(self):
        self.assertEqual(classifyTriangle('apple', 3, 4), 'InvalidInput')
        self.assertEqual(classifyTriangle(3, 'apple', 4), 'InvalidInput')
        self.assertEqual(classifyTriangle(3, 4, 'apple'), 'InvalidInput')

    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(0, 4, 1), "NotATriangle")
        self.assertEqual(classifyTriangle(1, 3, 5), "NotATriangle")
        self.assertEqual(classifyTriangle(7, 3, 2), "NotATriangle")

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 4, 5),'Right')
        self.assertEqual(classifyTriangle(5, 3, 4),'Right')
        self.assertEqual(classifyTriangle(4, 5, 3),'Right')

    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(4, 4, 7), 'Isosceles')
        self.assertEqual(classifyTriangle(100, 100, 150), 'Isosceles')

    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3, 5, 7), "Scalene")
        self.assertEqual(classifyTriangle(4, 5, 8), "Scalene")
        self.assertEqual(classifyTriangle(99, 100, 149), "Scalene")
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1, 1, 1),'Equilateral')
        self.assertEqual(classifyTriangle(199, 199, 199),'Equilateral')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

