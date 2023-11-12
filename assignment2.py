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
                print(f"{potions.getName()} was drunk!")
                drunk = True
                break
        if drunk == False:
            print("Potion was not found")
            

    def collectReagent(self, reagant, amount):
        if reagant == "Irit" or reagant == "Kwuarm" or reagant == "Cadantine" or reagant == "Lantadyme" or reagant == "Dwarf Weed" or reagant == "Arbuck" or reagant == "Avantoe":
            reagentInstance = Herb(reagant)
        if reagant == "Eye of Newt" or reagant == "Limpwurt Root" or reagant == "White Berries" or reagant == "Potato Cactus" or reagant == "Wine of Zamorak" or reagant == "Blood of Orcus" or reagant == "Ground Mud Rune" or reagant == "Grenwall Spike" or reagant == "Ground Miasma Rune":
            reagentInstance = Catalyst(reagant)
        
        self.__laboratory.addReagant(reagentInstance, amount)

    def refineReagent(self):
        Reagent.refineReagant()



class Laboratory():


    def __init__(self, potions = [], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        print(self.__herbs)
        print(self.__catalyst)

        potionName = type + " " + name

        if potionName == "Super Attack" or potionName == "Super Strength" or potionName == "Super Defence" or potionName == "Super Magic" or potionName == "Super Ranging" or potionName == "Super Necromancy":

            # NEEDS TO CHECK IF INGREDIANT IS IN LIST
            ingredientsValid = False
            primaryValid = False
            secondaryValid = False

            for herbs in self.__herbs:
                if herbs.getName() == primaryIngredient:
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == secondaryIngredient:
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
                self.__potions.append(potion)

                for ingrediant in self.__herbs:
                    if ingrediant.getName == primaryIngredient:
                        self.__herbs.remove(ingrediant)

                for ingrediant in self.__herbs:
                    if ingrediant.getName == secondaryIngredient:
                        self.__herbs.remove(ingrediant)

                print(self.__herbs)
                print(self.__potions)
                print(self.__catalyst)

            elif ingredientsValid == False:
                print(f"You do not have the correct ingrediants to make {potionName}")
                if primaryValid == False:
                    print(f"{primaryIngredient} Missing!")
                elif secondaryValid == False:
                    print(f"{secondaryIngredient} Missing!")


        elif potionName == "Extreme Attack" or potionName == "Extreme Strength" or potionName == "Extreme Defence" or potionName == "Extreme Magic" or potionName == "Extreme Ranging" or potionName == "Extreme Necromancy":
            

            ingredientsValid = False
            primaryValid = False
            secondaryValid = False
            

            for herbs in self.__herbs:
                if herbs.getName() == primaryIngredient:
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == primaryIngredient:
                    primaryValid = True
                    break

            for catalysts in self.__catalyst:
                if catalysts.getName() == secondaryIngredient:
                    secondaryValid = True 
                    break

            for potions in self.__potions:
                if (potions.getName()) == secondaryIngredient:
                    secondaryValid = True
                    break 

            if primaryValid == True and secondaryValid == True:
                ingredientsValid = True



            if ingredientsValid == True: 
                potion = ExtremePotion(primaryIngredient, secondaryIngredient, potionName, stat)
                self.__potions.append(potion)
                for herbs in self.__herbs:
                    if herbs.getName() == primaryIngredient: # Finds and removes the ingrediant
                        self.__herbs.remove(herbs)
                        break

                for catalysts in self.__catalyst:
                    if catalysts.getName() == primaryIngredient:
                        self.__catalyst.remove(catalysts)

                for catalysts in self.__catalyst:
                    if catalysts.getName() == secondaryIngredient:
                        self.__catalyst.remove(catalysts)

                for potions in self.__potions:
                    if potions.getName() == secondaryIngredient:
                        self.__potions.remove(potions)


            if ingredientsValid == False:
                print(f"You do not have the correct ingrediants to make {potionName}")


        else:
            print("Error")

       

    def addReagant(self, reagant, amount):
        reagantName = reagant.getName()
        print(reagantName)

        if reagantName == "Irit" or reagantName == "Kwuarm" or reagantName == "Cadantine" or reagantName == "Lantadyme" or reagantName == "Dwarf Weed" or reagantName == "Arbuck" or reagantName == "Avantoe": # Checks reagantName to see if it is a herb
            while amount > 0: # Every time a reagant is added to a list the amount is deducted.
                self.__herbs.append(reagant)
                amount -= 1

        if reagantName == "Eye of Newt" or reagantName == "Limpwurt Root" or reagantName == "White Berries" or reagantName == "Potato Cactus" or reagantName == "Wine of Zamorak" or reagantName == "Blood of Orcus" or reagantName == "Ground Mud Rune" or reagantName == "Grenwall Spike" or reagantName == "Ground Miasma Rune": # Checks reagantName to see if it is a catalyst
            while amount > 0:
                self.__catalyst.append(reagant)
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
        pass
    
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
        elif self.__name == "Extreme Attack" or self.__name == "Extreme Strength" or self.__name == "Extreme Defence" or self.__name == "Extreme Magic" or self.__name == "Extreme Ranging" or self.__name == "Extreme Necromancy":
            self.__boost = 0
        else:
            print("Error")
    
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
        potencyValue = Herb.herbDictionary.get(self.__name) # Retrieves potency
        potency = int(potencyValue)
        potency *= 2.5 # Calculates new potency
        Reagent.setPotency(self, potency)
        print(f"Potency is now: {potency}")

    def getGrimy(self):
        return self.__grimy

    def setGrimy(self, grimy = bool): # Passes True into a bool which returns False
        self.__grimy = grimy

    grimy = property(getGrimy, setGrimy) # Might not be required
      


class Catalyst(Reagent):

    catalystDictionary = {"Eye of Newt" : [4.3, 1.0], "Limpwurt Root" : [3.6, 1.7], "White Berries" : [1.2, 2.0], "Potato Cactus" : [7.3, 0.1], "Wine of Zamorak" : [1.7, 5.0], "Blood of Orcus" : [4.5, 2.2], "Ground Mud Rune" : [2.1, 6.7], "Grenwall Spike" : [6.3, 4.9], "Ground Miasma Rune" : [3.3, 5.2] }

    def __init__(self, name="name", quality = 0.0):
        super().__init__(name)
        self.__quality = quality

    def refine(self):
        values = Catalyst.catalystDictionary.get(self.__name)
        quality = int(values[1])
        potency = int(values[0])
        Reagent.setPotency(self, potency)
        if quality >= 8.9: # Tests quality and sets quality to quality+1.1 and checks if its at max(10) - outputs message.
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
test.collectReagent("Irit", 2)
test.collectReagent("Avantoe", 1)
test.collectReagent("Eye of Newt", 1)





#test.collectReagent("Irit", 2)
test.mixPotion("Super Attack")
test.mixPotion("Extreme Attack")
test.drinkPotion("Extreme Attack")
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


#Herbs with their potency value:
#Arbuck 2.6
#Avantoe 3.0
#Cadantine 1.5
#Dwarf Weed 2.5
#Irit 1.0
#Kwuarm 1.2
#Lantadyme 2.0
#Torstol 4.5

#Catalysts with their potency and quality value:
#Eye of Newt 4.3, 1.0
#Limpwurt Root 3.6, 1.7
#White Berries 1.2, 2.0
#Potato Cactus 7.3, 0.1
#Wine of Zamorak 1.7, 5.0
#Blood of Orcus 4.5, 2.2
#Ground Mud Rune 2.1, 6.7
#Grenwall Spike 6.3, 4.9
#Ground Miasma Rune 3.3, 5.2