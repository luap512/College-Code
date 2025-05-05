# Paul Perez
# September 16 2021
# Project 3
# COMPLETED
#---------------------------------------------------------------------------------
# The professor enters 3 grades.
# The program calculates the average of the grades.
# The program finds the letter grade based on the following grade scale
# If grade is 90 or more -> Letter Grade A
# If grade is between 80 and 90 -> Letter Grade B 
# If grade is between 70 and 80 -> Letter Grade C
# If grade is between 60 and 70 -> Letter Grade D 
# If grade is below 60 -> Letter Grade F
# The program displays the average grades and the letter grade with appropriate labels.
# Make sure to use main(), and few more functions
# ------------------------------------------------------------------------------



# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users function
    gradeOne = getIntegerData('enter your Math grade: ')
    gradeTwo = getIntegerData('enter your English grade: ')
    gradeThree = getIntegerData('enter your Programming grade: ')

    
    
    
    # assign the value associated by the calculate function to the variable 'gradeAvg'
    gradeAvg = doCalculate(gradeOne, gradeTwo, gradeThree)
    



    # call display function
    displayResult(gradeAvg, gradeOne, gradeTwo, gradeThree)
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------PROJECT 3-----------------------------------')
    print('-----------calculates GPA based on three user inputs.---------')
    print('--------------------------------------------------------------')
    

# This function calculates the grade    
def doCalculate(gradeOne, gradeTwo, gradeThree):
    value = ((gradeOne + gradeTwo + gradeThree)/3) # calculate GPA
    return value

    
        
# This fucntion displays the results
def displayResult(gradeAvg, gradeOne, gradeTwo, gradeThree):
    print('\nYou earned a', format(gradeOne,'.02f'),'in Math, a',format(gradeTwo,'.02f'),'in English and a', format(gradeThree,'.02f'),'in programming.')
    print('You earned an average of', format(gradeAvg,'.02f'))

    # if/else tree that prints the grade based on calculate gradeAvg.
    if(gradeAvg >= 90):
        print('\nYou got an A! \nNice work, nerd.')

    elif(gradeAvg >= 80):
        print('\nYou got a B. \nNot bad.')

    elif(gradeAvg >= 70):
        print('\nyou got a C. :/')

    elif(gradeAvg >= 60):
        print('\nyou got a D. \nCmon man.')

    else:
        print('\nYou failed \n:(')
    
    
    
    

# gets grade data from users
def getIntegerData(prompt):
    value = float(input(prompt))
    return value
    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






