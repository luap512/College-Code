# Paul Perez
# NOVEMBER 11 2021
# Classwork 140
# COMPLETED
#---------------------------------------------------------------------------------
# create a class Triangle. It will have 3 sides: 3, 4, 5. Write a method
# that will find and print the perimeter of the triangle.
# create an object myTriangle that will print the perimeter using the method of the object
# -------------------------------------------------------------------------

# create class
class Triangle:
    side1 = 3
    side2 = 4
    side3 = 5

    

    def printMe(self): # need to use self
        perimeter = self.side1 + self.side2 + self.side3
        print('The perimeter is: ',perimeter)


# this function runs our main objective
def main():

    myTriangle = Triangle()
    myTriangle.printMe()

    
    



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






