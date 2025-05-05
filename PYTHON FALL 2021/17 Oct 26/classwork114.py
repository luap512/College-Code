# Paul Perez
# OCTOBER 26 2021
# Classwork 113
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Create a menu with the following items
# A to add students; G to get letter grade
# for G users will 1 numeric grade; it will print the letter grade
# E will display all students and exit the menu
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    studentInfo = {'Paul':'A', 'Shelby':'A', 'AllyBaba':'F'} # create dictionary

    print('Student info: ',studentInfo)

    studentInfo['AllyBaba'] = 'C' # edit dictionary

    print('Student info: ',studentInfo)

    
    
    

        

    
    

    
        


    

    

   






   








# This function creates the menu    
def menu():
    print()
    print('            ==PAYROLL FUNCTIONS==')
    print('\t A----- Add Students')
    print('\t G----- Edit Grade')
    print('\t E----- Display Students and Exit')
    
    



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


# this function will get STRING data from users {commands: A, G, or E}
def getStringData(prompt):
    while (True):
        menu() # call menu
        value = input(prompt)
        value = value.upper()

        if (value in ['A', 'G', 'E']):
            return value
        else:
            print('Invalid entry. try again')




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






