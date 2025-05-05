# AllyBaba
# October 14, 2021
# Class Work 85
# WIP
# -----------------------------------------------------
# Lists - reading a file
# display all the data at one time
# display the count and sum of all numbers
# -----------------------------------------------------
def main():
    header()

    myList = []

    fileRead = open('data.txt', 'r')

    for line in fileRead:
        newLine = line.strip('\n')
        value = int(newLine)
        myList.append(value)
    
    fileRead.close()

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
