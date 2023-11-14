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

    def mixPotion(self, recipe): # recipe (potionName) looks inside of recipe dictionary and retrieves the key values (ingrediants)
        ingredients = self.__recipes.get(recipe) # Pulls the values outside of the dictionary into a list
        primary = str(ingredients[0]) # Breaks list into 2 string values
        secondary = str(ingredients[1])
        nameString = recipe.split() # Splits potionName into 2 strings EXAMPLE (Exteme) (Attack)
        potionName = str(nameString[0]) # Assigns each string to a new value
        type = str(nameString[1])
        
        if type == "Attack": # Checks type string (Attack) and assigns a stat value depending on the type name
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
        self.__laboratory.mixPotion(type, potionName, stat, primary, secondary) # Passes values to lab.mixPotion
        
    def drinkPotion(self, potion):
        drunk = False    
        for potions in self.__laboratory._Laboratory__potions: #Checks potions list for the potion name that was passed in. This method was used because there is no getter method in the uml diagram.
            if potions.getName() == potion:
                self.__laboratory._Laboratory__potions.remove(potions) #Removes potion from the list
                print(f"----------------------------\n{potions.getName()} was drunk!\n----------------------------")
                drunk = True
                type = potions.getName().split()

                if type[1] == "Attack": # Checks type string (Attack) and assigns a stat value depending on the type name
                    self.__attack = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0
                    
                    print(f"Your {type[1]} is now: {self.__attack}")


                elif type[1] == "Strength":
                    self.__strength = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0

                    print(f"Your {type[1]} is now: {self.__strength}")


                elif type[1] == "Defence":
                    self.__defence = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0

                    print(f"Your {type[1]} is now: {self.__defence}")


                elif type[1] == "Magic":
                    self.__magic = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0

                    print(f"Your {type[1]} is now: {self.__magic}")


                elif type[1] == "Ranging":
                    self.__ranged = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0

                    print(f"Your {type[1]} is now: {self.__ranged}")


                elif type[1] == "Necromancy":
                    self.__necromancy = potions.getBoost()
                    Value = potions.getBoost()
                    if self.__attack >= 101:
                        self.__attack = 100
                    elif self.__attack <= 0:
                        self.__attack = 0

                    print(f"Your {type[1]} is now: {self.__necromancy}")


                else:
                    print("Error")


                break
        if drunk == False:
            print("Potion was not found")


            

    def collectReagent(self, reagant, amount):
        self.__laboratory.addReagant(reagant, amount)

    def refineReagent(self):
        for reagent in self.__laboratory._Laboratory__herbs:
            Herb.refine(reagent)
        for reagent in self.__laboratory._Laboratory__catalyst:
            Catalyst.refine(reagent)



class Laboratory():
    def __init__(self, potions = [], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):


        potionName = type + " " + name

        if potionName == "Super Attack" or potionName == "Super Strength" or potionName == "Super Defence" or potionName == "Super Magic" or potionName == "Super Ranging" or potionName == "Super Necromancy":

            # NEEDS TO CHECK IF INGREDIANT IS IN LIST
            ingredientsValid = False
            primaryValid = False
            secondaryValid = False

            for herbs in self.__herbs:
                if herbs.getName() == primaryIngredient: # herbs are stored as memory values and the getter is used to get their name to compare. 
                    primaryIngredient = herbs
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == secondaryIngredient:
                    secondaryIngredient = catalysts
                    secondaryValid = True
                    break

            if primaryValid == True and secondaryValid == True:
                ingredientsValid = True
            if primaryValid == False:
                    print(f"{primaryIngredient} Missing!")
            if secondaryValid == False:
                print(f"{secondaryIngredient} Missing!")


            if ingredientsValid == True:
                potion = SuperPotion(primaryIngredient, secondaryIngredient, potionName, stat)
                potion.calculateBoost()
                self.__potions.append(potion)

                self.__herbs.remove(primaryIngredient)
                self.__catalyst.remove(secondaryIngredient)


            elif ingredientsValid == False:
                print(f"You do not have the correct ingrediants to make {potionName}")
                if primaryValid == False:
                    print(f"{primaryIngredient} Missing!")
                elif secondaryValid == False:
                    print(f"{secondaryIngredient} Missing!")


        elif potionName == "Extreme Attack" or potionName == "Extreme Strength" or potionName == "Extreme Defence" or potionName == "Extreme Magic" or potionName == "Extreme Ranging" or potionName == "Extreme Necromancy":
            
            # NEEDS TO CHECK IF INGREDIANT IS IN LIST
            ingredientsValid = False
            primaryValid = False
            secondaryValid = False
            
            for herbs in self.__herbs:
                if herbs.getName() == primaryIngredient:
                    primaryIngredient = herbs
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == primaryIngredient:
                    primaryIngredient = catalysts
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == secondaryIngredient:
                    secondaryIngredient = catalysts
                    secondaryValid = True 
                    break

            for potions in self.__potions:
                if potions.getName() == secondaryIngredient:
                    secondaryIngredient = potions
                    secondaryValid = True
                    break 

            if primaryValid == True and secondaryValid == True:
                ingredientsValid = True


            if ingredientsValid == True: 
                potion = ExtremePotion(primaryIngredient, secondaryIngredient, potionName, stat)
                potion.calculateBoost()
                secondaryIngredient.getBoost()
                self.__potions.append(potion)
                for herbs in self.__herbs:
                    if herbs.getName() == primaryIngredient.getName(): # Finds and removes the ingrediant
                        self.__herbs.remove(herbs)
                        break

                for catalysts in self.__catalyst:
                    if catalysts.getName() == primaryIngredient.getName():
                        self.__catalyst.remove(catalysts)

                for catalysts in self.__catalyst:
                    if catalysts.getName() == secondaryIngredient.getName():
                        self.__catalyst.remove(catalysts)

                for potions in self.__potions:
                    if potions.getName() == secondaryIngredient.getName():
                        self.__potions.remove(potions)


            if ingredientsValid == False:
                print(f"You do not have the correct ingrediants to make {potionName}")


        else:
            print("Error")

       

    def addReagant(self, reagant, amount):
        if reagant == "Irit" or reagant == "Kwuarm" or reagant == "Cadantine" or reagant == "Lantadyme" or reagant == "Dwarf Weed" or reagant == "Arbuck" or reagant == "Avantoe":
            reagentInstance = Herb(reagant)
            while amount > 0:
                self.__herbs.append(reagentInstance)
                amount -= 1
        if reagant == "Eye of Newt" or reagant == "Limpwurt Root" or reagant == "White Berries" or reagant == "Potato Cactus" or reagant == "Wine of Zamorak" or reagant == "Blood of Orcus" or reagant == "Ground Mud Rune" or reagant == "Grenwall Spike" or reagant == "Ground Miasma Rune":
            reagentInstance = Catalyst(reagant)
            while amount > 0:
                self.__catalyst.append(reagentInstance)
                amount -= 1



class Potion(ABC):
    def __init__(self, name = "name", stat = 0, boost = 1.0):
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
    def __init__(self, herb, catalyst, name="name", stat=0, boost=1.0): 
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        herbPotency = self.__herb.getPotency()
        catalystPotency = self.__catalyst.getPotency()

        final_boost = (herbPotency + catalystPotency) + 1.5
        self.boost = final_boost

    
    def getHerb(self):
        return self.__herb

    def getCatalist(self):
        return self.__catalyst



class ExtremePotion(Potion):
    def __init__(self, reagant, potion, name="name", stat=0, boost=1.0 ):
        super().__init__(name, stat, boost)
        self.__reagant = reagant
        self.__potion = potion

    def calculateBoost(self):
        primaryPotency = self.__reagant.getPotency()
        secondaryPotency = self.__potion.getBoost()
        print(secondaryPotency)
        print(primaryPotency)
        finalBoost = round(primaryPotency * secondaryPotency * 1.5, 2)

        self.boost = finalBoost

    
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
    herbDictionary = {"Arbuck": [2.6], "Avantoe": [3.0], "Cadantine": [1.5], "Dwarf Weed": [2.5], "Irit": [1.0], "Kwuarm": [1.2], "Lantadyme": [2.0], "Torstol": [4.5]}

    def __init__(self, name="name", grimy = True):
        super().__init__(name) 
        self.__grimy = grimy

    def refine(self):
        self.setGrimy(False)
        potencyValue = Herb.herbDictionary.get(self.getName()) # Retrieves potency
        potency = float(potencyValue[0])
        potency *= 2.5 # Calculates new potency
        self.setPotency(potency)
        print(f"{self.getName()}'s potency is now at: {round(potency, 2)}")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy = bool): # Passes True into a bool which returns False
        self.__grimy = grimy

      


class Catalyst(Reagent):
    catalystDictionary = {"Eye of Newt" : [4.3, 1.0], "Limpwurt Root" : [3.6, 1.7], "White Berries" : [1.2, 2.0], "Potato Cactus" : [7.3, 0.1], "Wine of Zamorak" : [1.7, 5.0], "Blood of Orcus" : [4.5, 2.2], "Ground Mud Rune" : [2.1, 6.7], "Grenwall Spike" : [6.3, 4.9], "Ground Miasma Rune" : [3.3, 5.2] }

    def __init__(self, name="name", quality = 0.0):
        super().__init__(name)
        self.__quality = quality

    def refine(self):
        values = Catalyst.catalystDictionary.get(self.getName())
        quality = float(values[1])
        potency = float(values[0])
        if quality >= 8.9: # Tests quality and sets quality to quality+1.1 and checks if its at max(10) - outputs message.
            self.__quality = 10
            quality = self.__quality
            print(round(quality, 2), " it cannot be refined any further")
        else:
            quality += 1.1 
            self.__quality = quality 
            print(f"{self.getName()}'s quality is now at: {round(quality, 2)}")

        boostPotency = quality * potency
        self.setPotency(boostPotency)
          

    def getQuality(self):
        return self.__quality



test = Alchemist()
testLab = Laboratory()
test.collectReagent("Irit", 2)
test.collectReagent("Avantoe", 1)
test.collectReagent("Eye of Newt", 1)
test.collectReagent("Arbuck", 1)
test.collectReagent("Blood of Orcus", 1)
test.refineReagent()
#test.collectReagent("Irit", 2)
test.mixPotion("Super Necromancy")
#test.mixPotion("Extreme Attack")
test.drinkPotion("Super Necromancy")
#test.drinkPotion("Super Attack")



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
# if 0 <= stength <=100:

