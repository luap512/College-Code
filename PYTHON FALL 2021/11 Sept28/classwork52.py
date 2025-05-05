# Paul Perez
# September 28 2021
# Classwork 53
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: FOR LOOP
# For loop:
# print all even numbers between 1 and 100 using for statement
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function





    # initialize the variables
    for counter in range(1, 101): # Print form 1 to 100
        if (counter % 2 == 0):
            print(counter)
    

    
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






