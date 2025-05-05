# Paul Perez
# September 21 2021
# Classwork 34
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: use WHILE statement to create an iterated list
# While statement
# While (condition):
#       statements - execute only when statement is true
# counter: defined before while loop and incrimented by 1 inside the scope of while loop
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    counter = 1
    while (counter <= 30):
        print('I am a mf legend in this bitch. Im a fuckin young genius savage')
        counter = counter + 1 #incriment by one

    
    
   
    
    
 
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 34-------------------------------')
    print('----create an iterated list using a while loop----------------')
    print('--------------------------------------------------------------')
        


# this funtion gets Float data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






