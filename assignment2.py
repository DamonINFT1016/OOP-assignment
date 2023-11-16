'''
File: .py
Description: 
Author: Damon Eccles
StudentID: 110401198
EmailID: eccdc001@mymail.edu.au
This is my own work as defined by the University's Academic Misconduct Policy.
'''


from abc import ABC, abstractmethod



class Alchemist():
    '''
    The alchemist class is the main class of the program. 
    In this class the user directly interacts by calling mixPoton, drinkPotion, collectreagant, refinereagant.
    '''
    def __init__(self, attack = 0, strength = 0, defence = 0, magic = 0, ranged = 0, necromancy = 0, recipes={"Super Attack": ["Irit","Eye of Newt"], "Super Strength" : ["Kwuarm", "Limpwurt Root"], "Super Defence": ["Cadantine", "White Berries"], "Super Magic": ["Lantadyme", "Potato Cactus"], "Super Ranging": ["Dwarf Weed","Wine of Zamorak"], "Super Necromancy" : ["Arbuck", "Blood of Orcus"], "Extreme Attack": ["Avantoe", "Super Attack"], "Extreme Strength": ["Dwarf Weed", "Super Strength"], "Extreme Defence": ["Lantadyme", "Super Defence"], "Extreme Magic": ["Ground Mud Rune", "Super Magic"], "Extreme Ranging": ["Grenwall Spike", "Super Ranging"], "Extreme Necromancy": ["Ground Miasma Rune", "Super Necromancy"]} ):
        self.__attack = attack
        self.__strength = strength
        self.__defence = defence
        self.__magic = magic
        self.__ranged = ranged
        self.__necromancy = necromancy
        self.__laboratory = Laboratory()
        self.__recipes = recipes
    
    def getLaboratory(self):
        return self.__laboratory

    def getRecipes(self):
        return self.__recipes

    def mixPotion(self, recipe): # recipe (potionName) looks inside of recipe dictionary and retrieves the key values (ingrediants)
        '''
        mixPotions is responsible for getting a recipe from the user and sorting through the dictionary of recipes to find the user input recipe.
        '''
        try:
            ingredients = self.__recipes.get(recipe) # Pulls the values outside of the dictionary into a list
            primary = str(ingredients[0]) # Breaks list into 2 string values
            secondary = str(ingredients[1])
            nameString = recipe.split() # Splits potionName into 2 strings EXAMPLE (Exteme) (Attack)
            potionName = str(nameString[0]) # Assigns each string to a new value
            type = str(nameString[1])
        except TypeError as exception:
            print(f"Error caught:  {exception}")
        
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
        '''
        Drink potion is responsible for getting the requested drink from the laboratory potions list and consuming it. Stats are added to the alchemist and the potion is removed from the inventory.
        '''
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
                    
                    print(f"Your {type[1]} skill is now: {self.__attack}")


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


            

    def collectReagant(self, reagant, amount = 1):
        '''
        collectReagant is responsible telling the laboratory addReagant method which reagant the user has picked up (passed in).
        '''
        self.__laboratory.addReagant(reagant, amount)

    def refineReagant(self):
        '''
        Loops through herbs list and catalyst list from Laboratory and sends each object to a refine method. 
        '''
        for reagant in self.__laboratory._Laboratory__herbs:
            Herb.refine(reagant)
        for reagant in self.__laboratory._Laboratory__catalyst:
            Catalyst.refine(reagant)



class Laboratory():
    '''
    The laboratory class is responsible for inventory management and the construction of potion, herb and catalyst object creation.
    This class is a composite class owned by alchemist. 
    Potions and Reagants have an association relationship with Laboratory
    '''
    def __init__(self, potions = [], herbs = [], catalyst = [] ):
        self.__potions = potions 
        self.__herbs = herbs
        self.__catalyst = catalyst

    def mixPotion(self, name, type, stat, primaryIngredient, secondaryIngredient):
        '''
    
        '''
        potionName = type + " " + name

        if potionName == "Super Attack" or potionName == "Super Strength" or potionName == "Super Defence" or potionName == "Super Magic" or potionName == "Super Ranging" or potionName == "Super Necromancy":

            # NEEDS TO CHECK IF INGREDIENT IS IN LIST
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
        '''
        This class takes the reagant and the amount from the alchemist collectReagant method and makes them into objects. These objects are then stored into the Herb or Catalyst list.
        '''

        if reagant == "Irit" or reagant == "Kwuarm" or reagant == "Cadantine" or reagant == "Lantadyme" or reagant == "Dwarf Weed" or reagant == "Arbuck" or reagant == "Avantoe":
            reagantInstance = Herb(reagant)
            while amount > 0:
                self.__herbs.append(reagantInstance)
                amount -= 1
        if reagant == "Eye of Newt" or reagant == "Limpwurt Root" or reagant == "White Berries" or reagant == "Potato Cactus" or reagant == "Wine of Zamorak" or reagant == "Blood of Orcus" or reagant == "Ground Mud Rune" or reagant == "Grenwall Spike" or reagant == "Ground Miasma Rune":
            reagantInstance = Catalyst(reagant)
            while amount > 0:
                self.__catalyst.append(reagantInstance)
                amount -= 1



class Potion(ABC):
    '''
    Potion is a parent class for SuperPotion and ExtremePotion. 
    '''
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
    '''
    Super Potion takes a herb and catyst object from Laboratory.mixPotion.
    Using the objects potency values in a formula the super potion's boost is created using the boost property from Potion. 
    The object is created and passed back to Laboratory.mixPotion.
    SuperPotion is a child class of the Potion class.
    '''
    def __init__(self, herb, catalyst, name="name", stat=0, boost=1.0): 
        super().__init__(name, stat, boost)
        self.__herb = herb
        self.__catalyst = catalyst

    def calculateBoost(self):
        '''
        Takes passed in herb object and catalyst object's potency values and adds them and + 1.5.
        '''
        herbPotency = self.__herb.getPotency()
        catalystPotency = self.__catalyst.getPotency()

        final_boost = (herbPotency + catalystPotency) + 1.5
        self.boost = final_boost

    
    def getHerb(self):
        return self.__herb

    def getCatalist(self):
        return self.__catalyst



class ExtremePotion(Potion):
    '''
    Extreme potion takes a reagant object either herb or catalyst as the first ingredient then takes a super varient of the extreme potion its trying to make. 
    The super potion passed in as the second ingredient's boost is times by the first ingredient's potency value then x 1.5.
    Extreme potion object is created and passed back to Laboratory.mixPotion.
    Extreme potion is the child class of the Potion class. 
    '''
    def __init__(self, reagant, potion, name="name", stat=0, boost=1.0 ):
        super().__init__(name, stat, boost)
        self.__reagant = reagant
        self.__potion = potion

    def calculateBoost(self):
        '''
        Takes passed in reagant object and superPotion object's potency and boost values and times them and times 1.5.
        '''
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



class Reagant(ABC):
    '''
    reagant is the parent class of the Herb and Catalyst class. 
    reagant has an association relationship with the Lab
    '''
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


        


class Herb(Reagant):
    '''
    Inherits attributes from reagant.
    Used to create Herb objects.
    refines reagant's potency for a higher value potion boost. 
    '''
    herbDictionary = {"Arbuck": [2.6], "Avantoe": [3.0], "Cadantine": [1.5], "Dwarf Weed": [2.5], "Irit": [1.0], "Kwuarm": [1.2], "Lantadyme": [2.0], "Torstol": [4.5]}

    def __init__(self, name="name", grimy = True):
        super().__init__(name) 
        self.__grimy = grimy

    def refine(self):
        '''
        Sets grimy attribute to False, and potency (default 1.0) is times by 2.5.
        '''
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

      


class Catalyst(Reagant):
    '''
    Inherits attributes from reagant.
    Used to create Catalyst objects.
    refines reagant's potency and quality for a higher value potion boost. 
    '''
    catalystDictionary = {"Eye of Newt" : [4.3, 1.0], "Limpwurt Root" : [3.6, 1.7], "White Berries" : [1.2, 2.0], "Potato Cactus" : [7.3, 0.1], "Wine of Zamorak" : [1.7, 5.0], "Blood of Orcus" : [4.5, 2.2], "Ground Mud Rune" : [2.1, 6.7], "Grenwall Spike" : [6.3, 4.9], "Ground Miasma Rune" : [3.3, 5.2] }

    def __init__(self, name="name", quality = 0.0):
        super().__init__(name)
        self.__quality = quality

    def refine(self):
        '''
    
        '''
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

test.collectReagant("Irit", 2)
test.collectReagant("Avantoe", 1)
test.collectReagant("Eye of Newt", 1)
test.collectReagant("Arbuck", 1)
test.collectReagant("Blood of Orcus", 1)

test.refineReagant()

test.mixPotion("Super Necromancy")
test.drinkPotion("Super Necromancy")

