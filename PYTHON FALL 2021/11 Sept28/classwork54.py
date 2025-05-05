# Paul Perez
# September 28 2021
# Classwork 53
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Find the sum and count of all numbers between two given numbers
# entered by users
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    while(True):



        lowerLimit = getIntData('Enter the lower limit: ')
        upperLimit = getIntData('Enter the upper limit: ')
    
        sumNum = 0
        countNum = 0

        if(lowerLimit > upperLimit):
            print('Your lower limit is bigger than ypur upper limit. Try again, idiot.')
        else:
            break

# initialize count create a range for count to execute statements (for loop)
    for count in range(lowerLimit, (upperLimit + 1)):
        print(count)
        sumNum = sumNum + count
        countNum = countNum + 1
    print('The sum of these numbers is: ',sumNum)
    




   
    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 53-------------------------------')
    print('----FOR LOOP--------------------------------------------------')
    print('----------a loop----------------------------------------------')
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






