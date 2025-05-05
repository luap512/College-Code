# Paul Perez
# NOVEMBER 11 2021
# Classwork 130
# COMPLETED
#---------------------------------------------------------------------------------
# how many characters of each type in the sentence
# -------------------------------------------------------------------------



# this function runs our main objective
def main():

    myCharacter = {}
    userInput = input('enter a sentence: ')

    mySet = set(userInput)

    for elem in mySet:
        myCharacter[elem] = 0


    for char in userInput:
        myCharacter[char] += 1

    print(myCharacter)
    


    
    



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






