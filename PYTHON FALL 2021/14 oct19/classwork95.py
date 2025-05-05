# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Users will enter grades until a negative is entered
# find the average and count how many are over average
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    
    firstName = getStringData('Enter your first name: ')
    lastName = getStringData('Enter your last name: ')


    fullName = firstName + ',' + lastName


    print('Full name is: ', fullName)
    

    
    

    
        


    

    

   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 80-------------------------------')
    print('----REVIEW----------------------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")




# this function gets FLOAT data from users
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")



def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






