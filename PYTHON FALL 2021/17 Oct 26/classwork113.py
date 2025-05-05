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
    stuList = []
    
    

    while(True):
        cmd = getStringData('\nEnter a command:')

        if (cmd == 'A'):
            print('\nAdding Student')
            name = input('Enter name of student: ')
            stuList.append(name)
              
        elif(cmd == 'G'):
            numGrade = getFloatData('Enter numeric grade:')

            if(numGrade >= 90):
                letGrade = 'A'
            elif(numGrade >= 80):
                letGrade = 'B'
            elif(numGrade >= 70):
                letGrade = 'C'
            elif(numGrade >= 60):
                letGrade = 'D'
            elif(numGrade > 50):
                letGrade = 'F'
            print(name +"'s", 'grade is', letGrade)
              
        
        else:
            print('\n ==SUMMARY==')
            print('Student List: ', stuList)
            break
    

    
    

    
        


    

    

   






   








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


# this function will get commands: A, G, or E
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






