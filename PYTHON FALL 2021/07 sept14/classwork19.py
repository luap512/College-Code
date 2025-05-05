# Paul Perez
# September 14 2021
# Classwork 19
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Users enter two floating values
# Divide the float values and print
# format to two decimal places -> format(number,'.02f')
# add another function that will print the header
# ------------------------------------------------------------------------------

# this function runs our main objective
def main():
    header() # call the header functiom

    # getting data from users
    valueOne = float(input('Enter the first number: '))
    valueTwo = float(input('Enter the second number: '))
    
    # calculate. (division)
    result  = valueOne / valueTwo

    # Display results
    print('\n Results: ')
    print(valueOne, 'divided by',valueTwo,'is',format(result, '.02f'))
    
# This function prints the header of the project
def header():
    print('----------------------------------------------------------')
    print('------------------class work 20-------------------------')
    print('This program divides two float values provided by users---')
    print('----------------------------------------------------------')
    




main() # first line of execution, it calls function main()
print('\nEnd of Project')






