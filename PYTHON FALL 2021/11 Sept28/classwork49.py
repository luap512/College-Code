# Paul Perez
# September 28 2021
# Classwork 49
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: FOR LOOP
# For loop:
# for<variable name> in range(start, n): n starts at 0 and ends at (n-1)
# statements
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    for counter in range(50, 76): # Print form 50 to 75
       print(counter)
    

    
    


# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 48-------------------------------')
    print('----FOR LOOP--------------------------------------------------')
    print('----------a loop----------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






