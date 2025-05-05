# Paul Perez
# OCTOBER 11 2021
# Project 5
# COMPLETED
#---------------------------------------------------------------------------------
# Write a program that will display the how many positive and negative integers entered by users.  The user will use 0 to terminate the data entry.
# ------------------------------------------------------------------------------



# this function runs our main objective
def main():
    header() # call the header function

    intVal = getIntegerData('Enter an integer <0 will terminate program>')
    evenCount = 0
    oddCount = 0

    while(intVal != 0):
        intVal = getIntegerData('Enter an integer <0 will terminate program>')

        if(intVal % 2 == 0):
            evenCount += 1
        else:
            oddCount += 1

    displayData(evenCount, oddCount)




# This function prints the header of the project
def header():
    print('------------------------------------------------------------------------------')
    print('-------------------------PROJECT 5--------------------------------------------')
    print('----Write a program that will find the total, average, max, min of the  ------')
    print('---------------------------numbers from a data file---------------------------')
    print('------------------------------------------------------------------------------')


# gets integer data from users
def getIntegerData(prompt):
    value = int(input(prompt))
    return value

# gets float data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value

        
        
def displayData(evenCount, oddCount):
    print('\n-----------------------')
    print(evenCount,'even integers')
    print(oddCount,'odd integers')
    

    
    
    
    
    


    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






