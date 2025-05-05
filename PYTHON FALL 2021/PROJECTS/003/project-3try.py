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



    # Get value from users
    gradeOne = getIntegerData('enter first grade: ')
    gradeTwo = getIntegerData('enter second grade: ')
    gradeThree = getIntegerData('enter third grade: ')
    
    
    
    
    # Calculate grade
    gradeAvg = doCalculate(gradeOne, gradeTwo, gradeThree)
    



    # call display function
    displayResult(gradeAvg)
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 32-------------------------------')
    print('------uses function to get data from users--------------------')
    print('--------------------------------------------------------------')
    

# This function calculates the grade    
def doCalculate(gradeOne, gradeTwo, gradeThree):
    value = ((gradeOne + gradeTwo + gradeThree)/3)
    return value

    
        
# This fucntion displays the results
def displayResult(gradeAvg):
    print('\nYou earned an average of', format(gradeAvg,'.02f'))


    if(gradeAvg >= 90):
        print('You got an A')

    elif(gradeAvg >= 80):
        print('you got a B')

    elif(gradeAvg >= 70):
        print('you got a C')

    elif(gradeAvg >= 60):
        print('you got a D')

    else:
        print('You failed :(')
    
    
    
    

# this funtion gets grade data from users
def getIntegerData(prompt):
    value = float(input(prompt))
    return value
    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






