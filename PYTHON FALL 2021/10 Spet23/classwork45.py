# Paul Perez
# September 23 2021
# Classwork 45
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: users enter data until they enter a negative number
# a negative value will exit the loop
# a value that is used to exit a loop is called a sentinel value
# a loob controlled by a sentinel value:
# syntax:
# pre-read input statement
# while (condition based on sentinel value)
#       update-read input statement
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    value = getIntData('Enter an upper limit<negative integer will terminate entry>: ')
    

    # This will display the req. data sets and do the calculation
    while (value >= 0):
        # update-read statement
        value = getIntData('Enter an upper limit<negative integer will terminate entry>: ')
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






