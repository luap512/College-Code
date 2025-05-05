# Paul Perez
# September 16 2021
# Classwork 31
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will enter 2 integers and display the sum
# use a function to display results
# use a function to perform the calculation -doCalculate()
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users
    numOne = int(input('Enter an ineger: '))
    numTwo = int(input('Enter an integer: '))
   
    
    
    # Calculate grade
    sumNum = doCalculate(numOne, numTwo)




    # call display function
    displayResult(numOne, numTwo, sumNum )


    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 31-------------------------------')
    print('gets your age and cash on hand and determines if you can party')
    print('--------------------------------------------------------------')
    

# This function displays the results    
def displayResult(numOne, numTwo, sumNum):
    print('\nResult')
    print('The sum of', numOne,'and', numTwo,'is', sumNum)

# This fucntion calculates the sum
def doCalculate(numOne, numTwo):
    return numOne + numTwo

main() # first line of execution, it calls function main()
print('\nEnd of Project')






