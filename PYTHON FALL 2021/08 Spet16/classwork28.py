# Paul Perez
# September 16 2021
# Classwork 28
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will print "you are a winner' sum of integers is greater than 10; otherise
# it will display 'you are not fit to play'
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users
    intVal1 = int(input('Enter a number: '))
    intVal2 = int(input('Enter another number: '))
    
    

    print('\nResults')
    # Calculate
    if (intVal1 + intVal2 > 10):
              print('..........you are a winner')
    else:
            print('........you are not fit to play')
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 28-------------------------------')
    print('gets your age and cash on hand and determines if you can party')
    print('--------------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






