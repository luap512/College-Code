# Paul Perez
# September 23 2021
# Classwork 44
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: display all the multiples of seven
# between two values entered by user; upper limit and lower limit
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    upperLim = getIntData('Enter an upper limit: ')
    lowerLim = getIntData('Enter a lower limit: ')
    multiple = 7
    result = 0

    # This will display the req. data sets and do the calculation
    while (lowerLim <= upperLim):
        if ( lowerLim  %  multiple == 0):
            print (lowerLim)
        lowerLim = lowerLim + 1
     
# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 44-------------------------------')
    print('----Display all the multiples of seven between and upper -----')
    print('----------and lower limit-------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets Float data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






