# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Do simple math:
# adding all digits in a number
# 456 -> 15
# 123 -> 6
# 999 -> 27
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    sumDigits = 0
    valOne =  getIntegerData('Enter a number: ')

    stringValue = str(valOne)


    for ctr in stringValue:
        print(ctr)
        sumDigits = sumDigits + int(ctr)
    print(sumDigits)
        
    
       


  
    

    
    

    
        


    

    

   






   








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






