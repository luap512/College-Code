# AllyBaba
# October 14, 2021
# Class Work 89
# WIP
# -----------------------------------------------------
# Lists - input values until 0 is entered.  use this in a function
# display at one time (using a function
# passing by reference (address)
# -----------------------------------------------------
def main():
    header()

    myList = []

    populateList(myList)

    displayList(myList)

def populateList(myList):
    value = getIntegerData('Enter an integer <0 will kill the program>: ')

    while (value != 0):
        myList.append(value)
        value = getIntegerData('Enter an integer <0 will kill the program>: ')

# This fuction will display the list
def displayList(myList):
    print('\nResult')
    print('Values:', myList)
    
# This function will get int values from users (Generic functions to get int entry)
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print('Oops! That was not a valid number. Try again...')

# This FloatData(prompt):
def getFloatData(prompt):
    value = float(input(prompt))
    return value

# This function will print the header of the project
def header():
    print('--------5  -----------------------------------------------------')
    print('          Class Work 74\n')
    print('')
    print('..')
    print('--------------------------------------------------------------')

main() 
print('\nEnd of project')
