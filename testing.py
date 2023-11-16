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

class TestMixingPotion(unittest.TestCase):
    def testMixingPotion(self):
        test = Alchemist
        test.mixPotion(self, "Super Attack")



class TestDrinkPotion(unittest.TestCase):
    def testDrinkingPotion(self):
        test = Alchemist
        test.drinkPotion(self, "Super Attack")
        self.assertEqual(test._Alchemist__attack, 3.5)



class TestCollectReagant(unittest.TestCase):
    def testCollect(self):
        test = Alchemist
        test.collectReagant("Irit")
         



class TestRefineReagant(unittest.TestCase):
    def testRefine(self):
        test = Alchemist
        test.refineReagant(self)





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