# Paul Perez
# OCTOBER 12 2021
# Classwork 65
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: make a for loop 1-100
# display only the even numbers with label
# display 'I am threes' if the number is divisible by three, otherwise dsiplay 'I am nobody'
# display 'I am rich' if the number is divisible by eleven or display 'I am super rich'
# if the number is divisible by 19 or display 'Im super super rich' if the number is divisible
# by 29 otherwise display 'I am the poorest'
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    
    for counter in range(1, 101):
        if(counter % 2 == 0):
            print(counter,'is an even number')

        if(counter % 3 == 0):
            print('I am threes')
        else:
            print('I am nobody')

        if(counter % 11 == 0):
            print('I am rich')
        elif(counter % 19 == 0):
            print('I am suoer rich')
        elif(counter % 29 == 0):
            print('I am super super rich')
        else:
            print('I am the pooerest')
        


   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 64-------------------------------')
    print('----REVIEW----------------------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    intVal = int(input(prompt))
    return intVal

# this function gets FLOAT data from users
def getFloatData(prompt):
    floatVal = float(input(prompt))
    return floatVal

main() # first line of execution, it calls function main()
print('\nEnd of Project')






