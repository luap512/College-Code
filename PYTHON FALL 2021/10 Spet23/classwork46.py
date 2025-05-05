# Paul Perez
# September 23 2021
# Classwork 46
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: users enter data until they enter '-999'
# '-999' is a sentinel value
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    value = getIntData('Enter an upper limit<-999 will terminate entry>: ')
    

    # This will display the req. data sets and do the calculation
    while (value != -999):
        # update-read statement
        value = getIntData('Enter an upper limit<-999 will terminate entry>: ')
# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 46-------------------------------')
    print('----show example of a sentinel value; a value that exits -----')
    print('----------a loop----------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






