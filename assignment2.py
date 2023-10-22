'''
File: .py
Description: 
Author: Damon Eccles
StudentID: 110401198
EmailID: eccdc001@mymail.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''

from abc import ABC, abstractmethod


#@abstractmethod

class Alchemist():
    def __init__(self, attack = 0, strength = 0, defence = 0, magic = 0, ranged = 0, necromancy = 0, laboratory="laboratory", recipies={} ):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipies = recipies
    
    def getlaboratory(self):
        pass

    def getRecipies(self):
        pass

    def mixPotion(self, recipe):
        pass

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagent(self):
        pass



class Laboratory():
    def __init__(self, potions = [], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagant(self, reagant, amount):
        pass

    def grabReagent(self, name):
        pass

    def cleanHerbs(self):
        pass

    def refineCatalysts(self):
        pass



class Potion(ABC):
    def __init__(self, name = "name", stat = 0, boost = 0.0):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        pass

    def getStat(self):
        pass

    def getBoost(self):
        pass

    def setBoost(self, boost):
        pass



class SuperPotion(Potion):
    def __init__(self, herb, catalyst ,name="name", stat=0, boost=0): #possible problem with order of the items care
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        return super().calculateBoost() #Revise super method for abstractmethods
    
    def getHerb(self, herb):
        pass

    def getCatalist(self, catalist):
        pass



class ExtremePotion(Potion):
    def __init__(self, reagant, potion, name="name", stat=0, boost=0 ):#possible problem with order of the items care
        super().__init__(name, stat, boost)
        self.__reagant = reagant
        self.__potion = potion

    def calculateBoost(self):
        return super().calculateBoost() #Revise super method for abstractmethods
    
    def getReagant(self):
        pass

    def getPotion(self):
        pass



class Reagent(ABC):
    def __init__(self, name = "name", potency = 0.0):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        pass

    def getPotency(self):
        pass

    def setPotency(self, boost):
        pass



class Herb(Reagent):
    def __init__(self, name="name", potency=0, grimy = True):
        super().__init__(name, potency) 
        self.__grimy = grimy

    def getGrimy(self):
        pass

    def setGrimy(self, grimy:bool):
        pass

        



class Catalyst(Reagent):
    def __init__(self, name="name", potency=0, quality = 0.0):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        pass



