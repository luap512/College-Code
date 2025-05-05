# Paul Perez
# September 28 2021
# Classwork 61
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Reading a file with ineteger values
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function


    if cou
    counter = 0 #counter
    sumNumbers = 0 #accumulator
    
    fileRead = open('TextDoc1.txt', 'r')

    # read the content of the file
    for newLine in fileRead:
        newLine = newLine.strip('\n') # removes new line from each line read
                                   # always read a string just like input
        value = int(newLine)
        counter = counter + 1
        sumNumbers = sumNumbers + value
        print(value)

    print('\nThere are',counter,'values in the file.')
    print('sum of Values is',sumNumbers)
    fileRead.close()
    




   
    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 55-------------------------------')
    print('----open and read text doccument------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntData(prompt):
    intVal = int(input(prompt))
    return intVal

# this function gets FLOAT data from users
def getFloatData(prompt):
    floatVal = float(input(prompt))
    return floatVal

main() # first line of execution, it calls function main()
print('\nEnd of Project')






