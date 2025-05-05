# Paul Perez
# NOVEMBER 5 2021
# Project 8
# COMPLETED
#---------------------------------------------------------------------------------
# Write a program that will find the sum of the digits of an integer.

# Deliverables
# The user enters an integer
# The program finds the sum of the digits
# The program displays the sum with appropriate labels.
# ------------------------------------------------------------------------------



# this function runs our main objective
def main():
    header() # call the header function

    

    # initialize variables
    usrEnt = getStringData('Enter an integer: ')





    # functuon to find the sum of the numbers
    sumNum = findSum(usrEnt) 
    
 




    # Display data function
    displayData(sumNum)
    
    





# This function prints the header of the project
def header():
    print('------------------------------------------------------------------------------')
    print('----------------------***PROJECT 8***-----------------------------------------')
    print('----Write a program that will find the sum of the digits of an integer-------')
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
    
   


# This fucntion displays data
def displayData(sumNum):
    print('\n------------------------------------------------')
    print('The sum of the digits is: ',sumNum)
    
    
   


# this function finds the sum of the digits.
def findSum(usrEnt):
    sumNum = 0
    for digit in str(usrEnt):
        sumNum = sumNum + int(digit)
    return sumNum
    
    
    


    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






