# AllyBaba
# October 14, 2021
# Class Work 84
# WIP
# -----------------------------------------------------
# Lists - Enter data until you enter -999;
# display all the data at one time
# display the count and sum of all numbers
# -----------------------------------------------------
def main():
    header()

    myList = [] #empty

    value = getIntegerData('Enter an integer <-999 will terminate>: ')

    while(value != -999):
        myList.append(value)
        value = getIntegerData('Enter an integer <-999 will terminate>: ')

    countNumbers = len(myList)
    sumNumbers = sum(myList)

    print('\Result')
    print('The values:', myList)
    print('Count:', countNumbers)
    print('Sum:', sumNumbers)

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
