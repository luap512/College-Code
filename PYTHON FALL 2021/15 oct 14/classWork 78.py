# AllyBaba
# October 14, 2021
# Class Work 78
# WIP
# -----------------------------------------------------
# Lists - display the range of values
# -----------------------------------------------------
def main():
    header()

    myGrocery =[12, 34, 45, 33, 12, 99, 123, -23]                             

    print('The List:', myGrocery)

    countNumbers = len(myGrocery)
    sumNumbers = sum(myGrocery)
    maxValue = max(myGrocery)
    minValue = min(myGrocery)
    rangeValue = maxValue - minValue

    print('Count of numbers:', countNumbers)
    print('Sum of numbers:', sumNumbers)
    print('Max value in the data set:', maxValue)
    print('Max value in the data set:', minValue)
    print('Range of values in the data set:', rangeValue)
    
# This function will get int values from users (Generic functions to get int entry)
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print("Oops!  That was no valid number.  Try again...")

# This function will get float values from users (Generic functions to get float entry)
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
