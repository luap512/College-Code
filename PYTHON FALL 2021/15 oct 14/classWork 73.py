# AllyBaba
# October 14, 2021
# Class Work 73
# WIP
# -----------------------------------------------------
# Lists - display whether the numbers are odd or even
# -----------------------------------------------------
def main():
    header()

    myGrocery =[12, 34, 45, 33, 12, 99, 123, -23]                             

    print('The List:', myGrocery)

    for ctr in myGrocery:
        if (ctr % 2 == 0):
            print(ctr, "is an even number")
        else:
            print(ctr, "is an odd number")

    
    
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
