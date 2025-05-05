# Paul Perez
# OCTOBER 26 2021
# Classwork 115
# COMPLETED
#---------------------------------------------------------------------------------
# Goal:
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    studentInfo = {'007':['AllyBaba', 90,12,13, 'F']} # create dictionary
    countStudents = len(studentInfo)

    print('Student info: ',studentInfo.values())
    print('Student keys: ',studentInfo.keys())

    print('Number of students: ',countStudents)

    
    
    

        

    
    

    
        


    

    

   






   








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






