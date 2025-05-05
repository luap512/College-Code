# Paul Perez
# NOVEMBER 11 2021
# Classwork 149
# COMPLETED
#---------------------------------------------------------------------------------
# create addition class that adds two numbers
# 
# -------------------------------------------------------------------------

# create class
class Addition:

    def __init__(self, value1, value2):
        self.valueOne = value1
        self.valueTwo = value2

    
    # getter fucntion to retrieve data attributes
    def getValueOne(self):
        return self.valueOne

    def getValueTwo(self):
        return self.valueTwo

    def addMe(self):
        return self.valueOne + self.valueTwo
        


# this function runs our main objective
def main():

    number1 = getIntegerData('Enter integer one: ')
    number2 = getIntegerData('Enter integer two: ')
   
    mainNum = Addition(number1, number2)

    result = mainNum.addMe()

    print(result)
         



    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 120------------------------------')
    print('----WALLSTREET VIBES M80--------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")




# this function gets FLOAT data from users (POSITIVE ONLY)
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (value >= 0):
                return value

            else:
                print('\t\t grade must be greater than zero')
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


# this function will get STRING data from users {commands: B, D, or T}
def getStringData(prompt):
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in ['MALE', 'FEMALE']):
            return value.capitalize()
        else:
            print ('\t\t Opps! Wrong entry')
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






