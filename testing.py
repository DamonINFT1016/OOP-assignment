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

class TestMixPotion(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)



class TestRefineReagant(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

class TestCollectReagant(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

class TestLabMixPotion(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

    
class TestAddReagant(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

class TestSuperCalculateBoost(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)


class TestExtremeCalculateBoost(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)


class TestHerbRefine(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

class TestCatalystRefine(unittest.TestCase):
    def testGetRecipe(self):
        recipe = Alchemist.mixPotion("Super Attack")
        self.assertEqual("Super Attack", recipe)

unittest.main()


#alchemist.drinkPotion
#alchemist.refineReagant
#alchemist.collectReagant
#lab.mixPotion
#lab.addReagant
#superPotion.calculateBoost
#extremePotion.calculateBoost
#herb.refine
#catalyst.refine