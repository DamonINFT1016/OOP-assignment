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
    def __init__(self, attack = 0, strength = 0, defence = 0, magic = 0, ranged = 0, necromancy = 0, laboratory="laboratory", recipes={"Super Attack": ["Irit","Eye of Newt"], "Super Strength" : ["Kwuarm", "Limpwurt Root"], "Super Defence": ["Cadantine", "White Berries"], "Super Magic": ["Lantadyme", "Potato Cactus"], "Super Ranging": ["Dwarf Weed","Wine of Zamorak"], "Super Necromancy" : ["Arbuck", "Blood of Orcus"], "Extreme Attack": ["Avantoe", "Super Attack"], "Extreme Strength": ["Dwarf Weed", "Super Strength"], "Extreme Defence": ["Lantadyme", "Super Defence"], "Extreme Magic": ["Ground Mud Rune", "Super Magic"], "Extreme Ranging": ["Grenwall Spike", "Super Ranging"], "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]} ):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = laboratory
        self.__recipes = recipes
    
    def getlaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        ingredients = self.__recipes.get(recipe)
        primary = str(ingredients[0])
        secondary = str(ingredients[1])

        return primary + secondary

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagent(self):
        pass



class Laboratory():

    jim = Alchemist()

    def __init__(self, potions = ["Super Attack", "Super Strength", "Super Defence", "Super Magic", "Super Ranging", "Super Necromancy", "Extreme Attack", "Extreme Strength", "Extreme Defence", "Extreme Magic", "Extreme Ranging", "Extreme Necromancy"], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        pass

    def addReagant(self, reagant, amount):

        if reagant == "Irit" or reagant == "Kwuarm" or reagant == "Cadantine" or reagant == "Lantadyme" or reagant == "Dwarf Weed" or reagant == "Arbuck"or reagant == "Avantoe":
            while amount > 0:
                self.__herbs.append(reagant)
                amount -= 1
        if reagant == "Eye of Newt" or reagant == "Limpwurt Root" or reagant == "White Berries" or reagant == "Potato Cactus" or reagant == "Wine of Zamorak" or reagant == "Blood of Orcus" or reagant == "Ground Mud Rune" or reagant == "Grenwall Spike" or reagant == "Ground Miasma Rune":
            while amount > 0:
                self.__herbs.append(reagant)
                amount -= 1




class Potion(ABC):
    def __init__(self, name = "name", stat = 0, boost = 0.0):
        self.__name = name
        self.__stat = stat
        self.__boost = boost

    @abstractmethod
    def calculateBoost(self):
        pass

    def getName(self):
        return self.__name

    def getStat(self):
        return self.__stat

    def getBoost(self):
        return self.__boost

    def setBoost(self, boost):
        self.__boost = boost

    boost = property(getBoost, setBoost)



class SuperPotion(Potion):
    def __init__(self, herb, catalyst, name="name", stat=0, boost=0): #possible problem with order of the items care
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        if self.__name == "Super Attack" or self.__name == "Super Strength" or self.__name == "Super Defence" or self.__name == "Super Magic" or self.__name == "Super Ranging" or self.__name == "Super Necromancy":
            self.__boost = 0
        elif self.__name == "Extreme Attack" or self.__name == "Extreme Strength" or self.__name == "Extreme Defence" or self.__name == "Extreme Magic" or self.__name == "Extreme Ranging" or self.__name == "Extreme Necromancy":
            self.__boost = 0
        else:
            print("Error")
    
    def getHerb(self):
        return self.__herb

    def getCatalist(self):
        return self.__catalyst



class ExtremePotion(Potion):
    def __init__(self, reagant, potion, name="name", stat=0, boost=0 ):#possible problem with order of the items care
        super().__init__(name, stat, boost)
        self.__reagant = reagant
        self.__potion = potion

    def calculateBoost(self):
        if self.__name == "Super Attack" or self.__name == "Super Strength" or self.__name == "Super Defence" or self.__name == "Super Magic" or self.__name == "Super Ranging" or self.__name == "Super Necromancy":
                self.__boost = 0
    
    def getReagant(self):
        return self.__reagant

    def getPotion(self):
        return self.__potion



class Reagent(ABC):
    def __init__(self, name = "name", potency = 0.0):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, boost):
        self.__potency = boost

    potency = property(getPotency, setPotency)
        


class Herb(Reagent):
    def __init__(self, name="name", potency=0, grimy = True):
        super().__init__(name, potency) 
        self.__grimy = grimy

    def refine(self):
        pass

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy:bool):
        self.__grimy = grimy

    grimy = property(getGrimy, setGrimy)
      


class Catalyst(Reagent):
    def __init__(self, name="name", potency=0, quality = 0.0):
        super().__init__(name, potency)
        self.__quality = quality

    def refine(self):
        pass

    def getQuality(self):
        return self.__quality



test = Alchemist()

print(test.mixPotion("Super Attack"))