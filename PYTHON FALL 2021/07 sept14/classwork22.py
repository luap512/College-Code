# Paul Perez
# September 14 2021
# Classwork 22
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Users enter two floating values
# Divide the float values and print
# format to two decimal places -> format(number,'.02f')
# add another function that will print the header
# add another function that will print the result
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function


    # getting data from users
    valueOne = float(input('Enter the first number: '))
    valueTwo = float(input('Enter the second number: '))
    

    # calculate. (division)
    result  = valueOne / valueTwo


    # Display results
    displayResults(valueOne, valueTwo, result)
    



# This function prints the header of the project
def header():
    print('-------------------------------------------------------')
    print('------------------class work 22------------------------')
    print('This program divides two float values provided by users')
    print('-------------------------------------------------------')
    



# This function will display the results
def displayResults(valueOne, valueTwo, result):
    print('\nResult:')
    print(valueOne, 'divided by',valueTwo,'is',format(result, '.02f'))
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






