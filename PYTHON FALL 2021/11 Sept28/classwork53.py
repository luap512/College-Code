# Paul Perez
# September 28 2021
# Classwork 53
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: FOR LOOP
# For loop:
# find the sum and count of even numbers between two numbers (1-100) 
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    sumNum = 0
    countNum = 0
    




    # initialize the variables
    for counter in range(1, 101): # Print form 1 to 100
        if (counter % 2 == 0):
            print(counter)
            sumNum = sumNum + counter
            countNum = countNum + 1
    print('The sum of these numbers is: ',sumNum)
    print('the count of these numbers is: ',countNum)
    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 52-------------------------------')
    print('----FOR LOOP--------------------------------------------------')
    print('----------a loop----------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






