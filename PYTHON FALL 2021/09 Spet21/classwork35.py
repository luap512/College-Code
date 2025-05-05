# Paul Perez
# September 21 2021
# Classwork 34
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: use WHILE statement to display all numbers between 1 and 50
# While statement
# While (condition):
#       statements - execute only when statement is true
# counter: defined before while loop and incrimented by 1 inside the scope of while loop
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    counter = 69
    while (counter <= 420):
        print(counter, 'poops taken')
        counter = counter + 1 #incriment by one

    
    
   
# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 35-------------------------------')
    print('----list numbers 1-50 using while loop----------------')
    print('--------------------------------------------------------------')
        


# this funtion gets Float data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






