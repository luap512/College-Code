# Paul Perez
# September 16 2021
# Classwork 32
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will enter 2 integers and display the sum
# use a function to display results
# use a function to perform the calculation -doCalculate()
# use a getData() function
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users
    numOne = getIntegerData('enter 1st integer: ')
    numTwo = getIntegerData('enter 2nd integer: ')
   
    
    
    # Calculate grade
    doCalculate(numOne, numTwo)




    # call display function
    displayResult(numOne, numTwo, sumNum)


    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 32-------------------------------')
    print('------uses function to get data from users--------------------')
    print('--------------------------------------------------------------')
    

# This function displays the results    
def displayResult(numOne, numTwo, sumNum):
    print('\nResult')
    print('The sum of', numOne,'and', numTwo,'is', sumNum)

# This fucntion calculates the sum
def doCalculate(numOne, numTwo):
    sumNum = numOne + numTwo
    return sumNum



# this funtion gets Integer data from users
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






