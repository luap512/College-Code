# Paul Perez
# OCTOBER 12 2021
# Classwork 64
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Make a while loop from 1 - 100
# Display only the numbers which are multiples of 5
# Display 'I am multiple of 7' when the number is divisible by 7
# Display 'I am odd' if the number is odd. Otherwise, display 'I am even'
# Display 'I am threes' if the number is divisible by three or display 'I am nines' if the
# number is divisible by 9 or display 'I am elevens' if the number is divisible by
# eleven, otherwise display 'I am nobody' 
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    
    counter = 1

    while(counter <= 100):
        if(counter % 5 == 0):
            print(counter)

        if(counter % 7 == 0):
            print('I am a multiple of 7')

        if(counter % 2 != 0):
            print('I am odd')
        else:
            print('I am even')

        if(counter % 3 == 0):
            print('I am threes')
        elif(counter % 9 == 0):
            print('I am nines')
        elif(counter % 11 == 0):
            print('I am elevens')
        else:
            print('I am nobody')
    
        
        counter = counter + 1
        


   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 64-------------------------------')
    print('----REVIEW----------------------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    intVal = int(input(prompt))
    return intVal

# this function gets FLOAT data from users
def getFloatData(prompt):
    floatVal = float(input(prompt))
    return floatVal

main() # first line of execution, it calls function main()
print('\nEnd of Project')






