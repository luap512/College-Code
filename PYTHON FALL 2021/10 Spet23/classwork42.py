# Paul Perez
# September 23 2021
# Classwork 42
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: use WHILE statement to display all numbers between 1 and 100
# DISPLAY THE COUNT OF THOSE NUMBERS
# Display the sums of those numbers
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # initialize the variables
    counter = 1
    evenCount = 0
    evenSum = 0

    # This will display the req. data sets and do the calculation
    while (counter <= 100):
        if (counter % 2 == 0):
            print(counter)
            evenCount = evenCount + 1 # counting -> adding one to even count
            evenSum = evenSum + counter # accumulating the values of counter
        counter = counter + 1 #incriment by one

    print('\nResults')
    print('The count of the data set is:',evenCount)
    print('The sum of the data set is:',evenSum)
 
# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 42-------------------------------')
    print('----list evem numbers 1-100 using while loop----------------')
    print('--------------------------------------------------------------')
        


# this funtion gets Float data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






