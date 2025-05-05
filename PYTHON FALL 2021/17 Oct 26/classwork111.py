# Paul Perez
# OCTOBER 26 2021
# Classwork 112
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Create menu w following items:
# A to add employees; D to display employees; P to pay employees
# for P (enter hours worked and hourly pay) ; it will dsiplay gross pay
# E will display all employees and exit the menu.
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function
    empList = []
    
    menu() # call menu
    


    while(True):
        cmd = getStringData('\nEnter a command:')

        if (cmd == 'A'):
            print('\nAdding Employee')
            name = input('Enter an employee: ')
            empList.append(name)
              
        elif(cmd == 'D'):
            print('\nDisplay Employee')
            print('Employee List: ',empList)
        
        elif(cmd == 'P'):
            print('\nPay employee')
            hrsWorked = getFloatData('Enter hours worked: ')
            hrsPay = getFloatData('Enter hourly pay: ')

            if(hrsWorked > 40):
                grossPay = 40 * hrsPay + (hrsWorked - 40) * hrsPay * 1.5
                print('\nGross pay: ',format(grossPay, '.02f'))
            else:
                grossPay = hrsWorked * hrsPay
                print('\nGross pay: ',format(grossPay, '.02f'))
        
        else:
            print('\n ==SUMMARY==')
            print('Employee List: ', empList)
            print('Gross pay: $'+ format(grossPay, '.02f'))
            break
    

    
    

    
        


    

    

   






   








# This function creates the menu    
def menu():
    print()
    print('            ==PAYROLL FUNCTIONS==')
    print('\t A----- Add employees')
    print('\t P----- Pay employees')
    print('\t D----- Display employees')
    print('\t X----- Display employees and exit')
    



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


# this function will get commands: A, D, P or X
def getStringData(prompt):
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in ['A', 'D', 'P', 'X']):
            return value
        else:
            print('Invalid entry. try again')




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






