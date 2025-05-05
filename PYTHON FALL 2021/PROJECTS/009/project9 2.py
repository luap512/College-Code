# Paul Perez
# NOVEMBER 8 2021
# Project 9 
# COMPLETED
#---------------------------------------------------------------------------------
# Class Structure:
# The name of the class is Pet
# The data attributes 
# name (the name of a pet)
# animalType (the type of animal. Example ‘Dog’, ‘Cat’, ‘Bird’)
# age (for the pet’s age)
# The class should have constructor that assigns the data attributes to blank
# The methods for the class

# The setters
# setName - This method assigns a value to name
# setAnimalType - This method assigns a value to animalType
# setAge - This method assigns a value to age.
# setGender – This method assigns the gender

# The getters
# getName - This method returns the value of the name.
# getAnimalType - This method returns the value of the animalType.
# getAge - This method returns the value of the age.
# getGender – This method returns the gender


# The program creates an object of the class 
# The user enters the name, type, and age of his or her pet. 
# The program stores the data as the object’s attributes. 
# The program uses methods to save and retrieve the pet’s name, type, and age and
# display this data on the screen with appropriate labels.
# ------------------------------------------------------------------------------


# create class
class Pet:
    
    def __init__(self, name, animalType, age, gender):
        self.petName = name 
        self.petAnimalType = animalType 
        self.petAge = age 
        self.petGender = gender



 # getters to retrieve data attributes
    def getName(self):
        return self.petName

    def getAnimalType(self):
        return self.petAnimalType

    def getAge(self):
        return self.petAge

    def getGender(self):
        return self.petGender
        



     # setters to set data attributes
    def setName(self,name):
        self.name = name
        
    def setAnimalType(self, animalType):
        self.animalType = animalType
        
    def setAge(self, age):
        self.age = age
        
    def setGender(self, gender):
        self.gender = gender








   
        



# this function runs our main objective
def main():
    header() # call the header function

    # get user data
    name1 = getStringData('Enter your pets name: ')
    animalType1 = getAnimalTypeData('Enter your pet type(Dog, bird, cat): ')
    age1 = getIntegerData('Enter your pets age(years): ')
    gender1 = getGenderData('Enter your pets gender(male/female): ')


    # create object of class 'Pet' with attributes name1, animalType1, age1, gender1
    petObj = Pet(name1, animalType1, age1, gender1)


    # setters to set the attributes of the object based on user in
    petObj.setName(name1)
    petObj.setAnimalType(name1)
    petObj.setAge(name1)
    petObj.setGender(name1)
    
    
    # display data
    displayData(petObj)   





# This function prints the header of the project
def header():
    print('------------------------------------------------------------------------------')
    print('----------------------***PROJECT 9***-----------------------------------------')
    print('---------------OBJECT ORIENTED PROGRAMMING---------------------------oh yeah--')
    print('------------------------------------------------------------------------------')


# gets integer data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")

            

# gets float data from users
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")



# gets string data from users
def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")

            
# function gets gender data
def getGenderData(prompt):
    while (True):
        value = str(input(prompt))
        value = value.upper()

        if(value in ['MALE', 'FEMALE']):
            return value.capitalize()

        else:
            print('\t\t Invalid entry')




# function gets animalType data
def getAnimalTypeData(prompt):
    while (True):
        value = str(input(prompt))
        value = value.upper()

        if(value in ['DOG', 'CAT', 'BIRD']):
            return value.capitalize()

        else:
            print('\t\t Invalid entry')
   


# This fucntion displays data
def displayData(petObj):
    print('\n------------------------------------------------')
    print('Your',petObj.getGender(),petObj.getAnimalType(),'named',petObj.getName(),'is \n',petObj.getAge(),'years old.')
    
    
   



    
main() # first line of execution, it calls function main()
print('\nEnd of Project')






