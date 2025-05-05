# Paul Perez
# September 23 2021
# Classwork 48
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: users enter data until they enter '-999'
# '-999' is a sentinel value
# display how many numbers were entered by the users
# display the sum of the numbers
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    value = getIntData('Enter an upper limit<-999 will terminate entry>: ')
    counter = 0
    numSum = 0
    

    # This will display the req. data sets and do the calculation
    while (value != -999):
        # update-read statement
        counter = counter + 1
        numSum = numSum + value
        value = getIntData('Enter an upper limit<-999 will terminate entry>: ')
    print('\nyou entered',counter,'values')
    print('the sum of all the numbers is: ',numSum)


# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 48-------------------------------')
    print('----show example of a sentinel value; a value that exits -----')
    print('----------a loop----------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






