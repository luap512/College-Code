# Paul Perez
# September 16 2021
# Classwork 27
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will print "you are a winner' if inetegr is divisible two and five; otherise
# it will display 'you are not fit to play'
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users
    intVal = int(input('Enter a number: '))
    

    print('\nResults')
    # Calculate if number is even or odd
    if (intVal % 2 == 0 & intVal % 5 == 0):
              print(intVal,'you are a winner')
    else:
            print(intVal,'you are not fit to play')
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 27-------------------------------')
    print('gets your age and cash on hand and determines if you can party')
    print('--------------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






