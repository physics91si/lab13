#!/usr/bin/python

# Lab 13
# Physics 91SI
# Spring 2016

import unittest
import calc

class CalcTest(unittest.TestCase):
    # TODO implement tests here to verify that your functions work!
    def testAddition(self):
        self.assertEqual(calc.calc('1+1'), 2)

    def testSubtraction(self):
        pass

    def testMultiplication(self):
        pass
 
    def testDivision(self):
        pass

if __name__ == '__main__':
    unittest.main()

