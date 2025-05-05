# Paul Perez
# September 14 2021
# Classwork 24
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will get age data from users (integer a)
# evaluate 2a-4a+a
# if result is more than 10 display "youre a winner"
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # Get value from users
    a = int(input('Enter the value of a: '))

    # Evaluate the expression
    resultVal = 2 * a - 4 * a + a

    # Display result if more than 10
    if (resultVal >= 10):
              print('\nResult')
              print('You are the winner!!!')
    




# This function prints the header of the project
def header():
    print('-------------------------------------------------------')
    print('------------------class work 24------------------------')
    print('This program evaluates 2a-4a+a and compares result to 10')
    print('-------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






