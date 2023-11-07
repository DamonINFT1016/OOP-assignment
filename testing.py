'''
File: .py
Description: 
Author: Damon Eccles
StudentID: 110401198
EmailID: eccdc001@mymail.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

import unittest

from assignment2 import *

class TestGetRecipe(unittest.TestCase):
    def testGetRecipe(self):
        alchemist = Alchemist("Super Attack")
        self.assertEqual("Super Attack", alchemist.getRecipies())




unittest.main()