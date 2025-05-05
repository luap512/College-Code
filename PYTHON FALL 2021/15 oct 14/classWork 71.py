# AllyBaba
# October 14, 2021
# Class Work 71
# WIP
# -----------------------------------------------------
# Lists
# -----------------------------------------------------
def main():
    header()

    myGrocery =['Candy', 30, 'Tortillas', 23.99, 'Oreos', 55]
    # elements:    1      2      3          4       5      6
    # index        0      1      2          3       4      5
    # index        -6     -5     -4         -3      -2     -1                                        

    print('The List:', myGrocery)
    print('Michele"s request:', myGrocery[0])
    print('Michele"s owes me:', myGrocery[1])

    # access the 6th element left to right
    print('Shane owes me:', myGrocery[5])

    #access the 6th element  right to left
    print('Shane owes me:', myGrocery[-1])
    
    
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
    print('          Class Work 71\n')
    print('')
    print('..')
    print('--------------------------------------------------------------')

main() 
print('\nEnd of project')
