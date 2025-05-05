# Paul Perez
# September 14 2021
# Classwork 23
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will get age data from users
# if age is older than 100 then "you are old man"
# decision making -if
# syntax:
# if(condition):
#   statements will only execute if statement is true
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function


    # getting data from users
    age = int(input('Enter your age: '))

    if (age >= 100):
        print('you are an old man')
    
    




# This function prints the header of the project
def header():
    print('-------------------------------------------------------')
    print('------------------class work 23------------------------')
    print('This program divides two float values provided by users')
    print('-------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






