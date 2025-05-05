# Paul Perez
# September 23 2021
# Classwork 43
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: display the multiplication of user inputed integer from 1 to 10
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    counter = 0
    result = 0
    multiple = getIntData('enter an integer: ')
    
    # This will display the req. data sets and do the calculation
    while (counter <= 10):
        result = counter * multiple
        print(counter, 'times',multiple,'is equal to,',result)
        counter = counter + 1 #incriment by one
 
# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 42-------------------------------')
    print('----Display the multiplication of 7 from 1 to 10--------------')
    print('--------------------------------------------------------------')
        


# this funtion gets Float data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






