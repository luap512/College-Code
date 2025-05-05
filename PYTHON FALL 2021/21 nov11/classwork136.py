# Paul Perez
# NOVEMBER 11 2021
# Classwork 134
# COMPLETED
#---------------------------------------------------------------------------------
#Class
# -------------------------------------------------------------------------

# create class
class Triangle:
    sideOne = 0
    sideTwo = 0
    sideThree = 0


# this function runs our main objective
def main():

    myTriangle = Triangle()
    myTriangle.sideOne = 3
    myTriangle.sideTwo = 4
    myTriangle.sideThree = 5

    perimeter = myTriangle.sideOne + myTriangle.sideTwo + myTriangle.sideThree

    print(perimeter)
    
    
    

    
    



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
    value = input(prompt)
    value = value.upper()
    return value
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






