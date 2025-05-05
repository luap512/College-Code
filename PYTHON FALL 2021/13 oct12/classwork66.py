# Paul Perez
# OCTOBER 12 2021
# Classwork 65
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: users enter value until -999 is entered
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    
    value = getIntegerData('Enter a number <-999 will terminate>')




    while(value != -999):
        value = getIntegerData('Enter a number <-999 will terminate>')
        


   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 64-------------------------------')
    print('----REVIEW----------------------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            if (value >= 1 and value <=5):
                return value
            else:
                print('The integer is not between 1 and 5')
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")




# this function gets FLOAT data from users
def getFloatData(prompt):
    floatVal = float(input(prompt))
    return floatVal

main() # first line of execution, it calls function main()
print('\nEnd of Project')






