# Paul Perez
# OCTOBER 12 2021
# Classwork 69
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: The program will display all the integer values from a file
# named 'data.txt'. Display How many numbers are there. Display the sum of the numbers
# display the average of the numbers
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    sumNum = 0
    numAvg = 0
    counter = 0

    
    fileRead = open('data.txt', 'r')
    for line in fileRead:
        newLine = line.strip('\n')
        value = int(newLine)
        print(value)
        counter = counter + 1
        sumNum = sumNum + value

    numAvg = (sumNum / counter)
    print('The count of the numbers is ',counter)
    print('the sum of the numbers is ',sumNum)
    print('The average is: ',format(numAvg,'.02f'))
        
    fileRead.close()
    

    
        


   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 69-------------------------------')
    print('----REVIEW----------------------------------------------------')
    print('--------------------------------------------------------------')
    print('--------------------------------------------------------------')    


# this funtion gets INT data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")




# this function gets FLOAT data from users
def getFloatData(prompt):
    floatVal = float(input(prompt))
    return floatVal

main() # first line of execution, it calls function main()
print('\nEnd of Project')






