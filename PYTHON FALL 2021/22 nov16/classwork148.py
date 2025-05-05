# Paul Perez
# NOVEMBER 11 2021
# Classwork 148
# COMPLETED
#---------------------------------------------------------------------------------
# create a form that will accept name, gender, 
# -------------------------------------------------------------------------

# create class
class Student:

    def __init__(self, value1, value2, value3):
        self.name = value1
        self.gender = value2
        


# this function runs our main objective
def main():
   name = input('Enter your name: ')
   gender = getStringData('Enter your gender: ')
      
         



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
            return value
        else:
            print ('\t\t Opps! Wrong entry')
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






