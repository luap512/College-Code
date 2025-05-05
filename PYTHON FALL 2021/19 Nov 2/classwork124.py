# Paul Perez
# NOVEMBER 2 2021
# Classwork 124
# COMPLETED
#---------------------------------------------------------------------------------
# english word has spanish translation
# 
# -------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    translation = {} # empty dictionary


    for ctr in range (5):
        englishWord = getStringData('\nEnter english word: ')
        spanishWord = getStringData('enter spanish translation: ')
        translation[englishWord] = spanishWord # assign dictionary

    print('\n-----------------------------------------------------------')
    print('Word Bank: ',translation) # print dictionary



    
    



    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 120------------------------------')
    print('----WALLSTREET VIBES M80--------------------------------------')
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




# this function gets FLOAT data from users (POSITIVE ONLY)
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (value >= 0):
                return value

            else:
                print('\t\t grade must be greater than zero')
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


# this function will get STRING data from users {commands: B, D, or T}
def getStringData(prompt):
    value = input(prompt)
    value = value.upper()
    return value
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






