# Paul Perez
# September 21 2021
# PROJECT 4
# COMPLETED
#---------------------------------------------------------------------------------
# The user enters the upperLimit (an integers value)
# Use WHILE statement to display all numbers between 0 and upperLimit divisible by 7
# Use IF statement to find the numbers.
# The program displays the average of the numbers with appropriate labels.
# Make sure to use main(), and few more functions
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function


# call the fucntion get user data
    upperLimit = getIntegerData('Enter the upper limit: ')


# call the calculations function
    numAvg = doCalculate(upperLimit)
    

#call the display results function
    displayResult(numAvg)
   
# This function prints the header of the project
def header():
    print('-------------------------------------------------------------------')
    print('------------------PROJECT FOUR-------------------------------------')
    print('----find a list of all numbers below upper limit divisible by seven')
    print('----Then find the avergae------------------------------------------')
    print('-------------------------------------------------------------------')
        


# this funtion gets Float data from users
def getIntegerData(prompt):
    value = int(input(prompt))
    return value


# this function uses a 'while' and 'if' loop to find the #'s divisible by seven
def doCalculate(upperLimit):
    counter = 0
    numSum = 0
    sampleSize = 0
    print('Values between zero and',upperLimit,'that are divisible by seven: ')
    while (counter <= upperLimit):
        if (counter % 7 == 0):
            print(counter)
            numSum = numSum + counter
            sampleSize = sampleSize + 1 # count the amount of numbers that satisfy conditions 
        counter = counter + 1 # incriment by one (test next number)
    numAvg = (numSum / sampleSize)
    return numAvg

    

# display the average of the numbers divisible by seven
def displayResult(numAvg):
    print('\nThe average value of all these multiples of seven is: ',numAvg)
    



main() # first line of execution, it calls function main()
print('\nEnd of Project')






