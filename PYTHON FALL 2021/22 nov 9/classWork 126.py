# AllyBaba
# Nov 9, 2021
# Class Work 126
# WIP
# -----------------------------------------------------
# -----------------------------------------------------
def main():
    header()
    serviceCharge = 0
    
    balance = getFloatData('Enter initial balance: ')
    while (True):
        cmd = getStringData('Enter your selection: ')

        if (cmd == 'D'):
            amount = getFloatData('Enter amount to deposit: ')
            balance = calculate(cmd, balance, amount, serviceCharge)
             
        elif (cmd == 'W'):
            amount = getFloatData('Enter amount to withdraw: ')
            balance, serviceCharge = calculate(cmd, balance, amount, serviceCharge)
            
        else:
            print('\nMonthly Summary')
            displayResults(balance, serviceCharge)
            balance = balance - serviceCharge
            print('Final Balance: ', format(balance, '.02f'))
            break

# Thisfunction will do deposit/withdraw
def calculate(cmd, balance, amount, serviceCharge):
    if (cmd == 'D'):
        balance = balance + amount
        displayResults(balance, serviceCharge)
        return balance
    else:
        if (amount > balance):
            serviceCharge = serviceCharge + 20
        else:
            balance = balance - amount
            serviceCharge = serviceCharge + .25
        displayResults(balance, serviceCharge)
        return balance, serviceCharge

#This will display the results
def displayResults(balance, serviceCharge):
    print('Balance: ', format(balance, '.02f'))
    print('Accrued Service Charge: ', format(serviceCharge, '.02f'))
    
# This is the menu for the app
def menu():
    print('   AllyBaba Bank')
    print('\t D  ----  Deposit')
    print('\t W  ----  Withdraw')
    print('\t E  ----  Exit my app')
   
# This function will get commands: 
def  getStringData(prompt):
    while (True):
        menu()
        value = input(prompt)
        value = value.upper()

        if (value in ['W', 'D', 'E']):
            return value
        else:
            print ('\t\t Opps! Wrong entry')
    
        
# This function will get int values from users (Generic functions to get int entry)
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value

        except ValueError:
            print('Oops! That was not a valid number. Try again...')

# This FloatData(prompt): 
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (value > 0):
                return value
            else:
                print('\t\t No negative entry')

        except ValueError:
            print('Oops! That was not a valid number. Try again...')

# This function will print the header of the project
def header():
    print('--------5  -----------------------------------------------------')
    print('          Class Work 125\n')
    print('')
    print('..')
    print('--------------------------------------------------------------')

main() 
print('\nEnd of project')
