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
    def __init__(self, attack = 0, strength = 0, defence = 0, magic = 0, ranged = 0, necromancy = 0, recipes={"Super Attack": ["Irit","Eye of Newt"], "Super Strength" : ["Kwuarm", "Limpwurt Root"], "Super Defence": ["Cadantine", "White Berries"], "Super Magic": ["Lantadyme", "Potato Cactus"], "Super Ranging": ["Dwarf Weed","Wine of Zamorak"], "Super Necromancy" : ["Arbuck", "Blood of Orcus"], "Extreme Attack": ["Avantoe", "Super Attack"], "Extreme Strength": ["Dwarf Weed", "Super Strength"], "Extreme Defence": ["Lantadyme", "Super Defence"], "Extreme Magic": ["Ground Mud Rune", "Super Magic"], "Extreme Ranging": ["Grenwall Spike", "Super Ranging"], "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]} ):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory()
        self.__recipes = recipes
    
    def getlaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe):
        ingredients = self.__recipes.get(recipe)
        primary = str(ingredients[0])
        secondary = str(ingredients[1])

        nameString = recipe.split()
        potionName = str(nameString[0])
        type = str(nameString[1])
        if type == "Attack":
            stat = "attack"
        elif type == "Strength":
            stat = "strength"
        elif type == "Defence":
            stat = "defence"
        elif type == "Magic":
            stat = "magic"
        elif type == "Ranging":
            stat = "ranged"
        elif type == "Necromancy":
            stat = "necromancy"
        else:
            print("Error")



        self.__laboratory.mixPotion(potionName, type, stat, primary, secondary)
        

    def drinkPotion(self, potion):
        pass

    def collectReagent(self, reagent, amount):
        pass

    def refineReagent(self):
        Laboratory.addReagant()



class Laboratory():


    def __init__(self, potions = [], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):

        print(name)
        print(type)
        print(stat)
        print(primaryIngredient)
        print(secondaryIngredient)



    def addReagant(self, reagant, amount):

        reagantName = reagant.getName()
        print(reagantName)
        if reagantName == "Irit" or reagantName == "Kwuarm" or reagantName == "Cadantine" or reagantName == "Lantadyme" or reagantName == "Dwarf Weed" or reagantName == "Arbuck" or reagantName == "Avantoe":
            while amount > 0:
                self.__herbs.append(reagantName)
                amount -= 1
        if reagantName == "Eye of Newt" or reagantName == "Limpwurt Root" or reagantName == "White Berries" or reagantName == "Potato Cactus" or reagantName == "Wine of Zamorak" or reagantName == "Blood of Orcus" or reagantName == "Ground Mud Rune" or reagantName == "Grenwall Spike" or reagantName == "Ground Miasma Rune":
            while amount > 0:
                self.__catalyst.append(reagantName)
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
    def __init__(self, name = "name", potency = 1.0):
        self.__name = name
        self.__potency = potency

    @abstractmethod
    def refine(self):
        pass

    def getName(self):
        return self.__name

    def getPotency(self):
        return self.__potency

    def setPotency(self, potency):
        self.__potency = potency

    potency = property(getPotency, setPotency)
        


class Herb(Reagent):
    def __init__(self, name="name", grimy = True):
        super().__init__(name) 
        self.__grimy = grimy

    def refine(self):
        #Need to get name of herb and degrime the herb and multiply potency by 2.5x
        self.setGrimy(False)
        potency = Reagent.getPotency(self)
        potency *= 2.5
        Reagent.setPotency(self, potency)
        print(f"Potency is now: {potency}")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy = bool):
        self.__grimy = grimy

    grimy = property(getGrimy, setGrimy)
      


class Catalyst(Reagent):
    def __init__(self, name="name", quality = 0.0):
        super().__init__(name)
        self.__quality = quality

    def refine(self):
        quality = self.getQuality()
        if quality >= 8.9:
            self.__quality = 10
            quality = self.__quality
            print(quality, " it cannot be refined any further")
        else:
            quality += 1.1 
            self.__quality = quality 
            print(quality)

    def getQuality(self):
        return self.__quality



test = Alchemist()
testLab = Laboratory()

test.mixPotion("Super Attack")



# aggregrate interaction between laboratory and Reagant / Potion
# Same goes for potion
# Create Reagant than add it to a list we can then use that from laboratory
# EXAMPLE
#JimsLab = Laboratory()
#herb1 = Herb("Irit", True)
#JimsLab.addReagant(herb1, 2)
#herb1.refine()
#print(herb1.grimy)
#print(JimsLab.getHerbs())

#catalyst1 = Catalyst("Eye of Newt", 9.4)
#catalyst1.refine()
#JimsLab.addReagant(catalyst1, 2)
#"Super Attack", "Super Strength", "Super Defence", "Super Magic", "Super Ranging", "Super Necromancy", "Extreme Attack", "Extreme Strength", "Extreme Defence", "Extreme Magic", "Extreme Ranging", "Extreme Necromancy"

#TODO
#class Potion creation
#composition between lab and alchemist
#collectReagant - this needs to be the input that then leads addReagant inside of lab.
#Need to pass in the recipe ingrediants from inside alchemist mixPotions into Lab mixpotions as primary and secondary
#Calculate boost.
#Also need to distinguish non refined to refined reagants.
#reagants will eventually all be refined all at once.
#drink potion() - probably use a dictionary
#Testing
#Error Handling
# Doc strings
# if 0 <= stength <=:

