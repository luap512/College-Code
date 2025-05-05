# Paul Perez
# September 20 2021
# Project 3
# COMPLETED
#---------------------------------------------------------------------------------
# The user enters the upperLimit (an integers value)
# Use WHILE statement to display all numbers between 0 and upperLimit.
# Use IF statement to find the numbers.
# The program displays the average of the numbers with appropriate labels.
# Make sure to use main(), and few more functions
# ------------------------------------------------------------------------------



# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users function
    upperLimit = getIntegerData('Enter a whole number greater than zero: ')
    

    # assign the value associated by the calculate function to the variable 'gradeAvg'
    gradeAvg = doCalculate()
    

    # call display function
    displayResult()
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('-------------------------PROJECT 4----------------------------')
    print('-----------Calculates average of numbers divisible by 7-------')
    print('-----------between 0 and a user supplied integer--------------')
    print('--------------------------------------------------------------')



# gets grade data from users
def getIntegerData(prompt):
    value = float(input(prompt))
    return value







# This function calculates the grade    
def doCalculate(upperLimit):
    
   
    
        
# This fucntion displays the results
def displayResult():
    
    
    
    
    


    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






