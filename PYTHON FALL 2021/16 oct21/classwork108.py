# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Have a menu which will perfom certain operations
#           AllyBaba Crypto
#        B ----- to buy
#        S ----- to sell
#        X ----- to exit
# buy and sell using inital ammount
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    balance = getFloatData('Enter your initial investment: $')
    
    menu()

    while (True):        
        cmd = getStringData('Make your selection: ')

        if (cmd == "B"):
            print('\n Buying Crypto')
            howMuch = getFloatData('Enter Amount: $')
            balance = balance + howMuch
            
        elif (cmd == 'S'):
            print('\n you are selling')
            howMuch = getFloatData('Enter Amount: $')
            balance = balance - howMuch
            
        else:
            print('\n SUMMARY')
            print('Balance: ', format(balance, '.02f'))
            
            break
        
       


  
    

    
    

    
        


    

    

   






   








# This function creates the menu    
def menu():
    print()
    print('            AllyBaba Crypto')
    print('\t B----- to Buy')
    print('\t S----- to Sell')
    print('\t X----- to Exit')









    



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


# this function will get commands: B, S, or X
def getStringData(prompt):
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in ['B', 'S', 'X']):
            return value
        else:
            print('Invalid entry. try again')




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






