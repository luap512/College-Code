# Paul Perez
# OCTOBER 11 2021
# Project 6
# COMPLETED
#---------------------------------------------------------------------------------
# The program reads integers from a txt file.
# While reading, the program stores the integers in a list.
# The program displays the count, total, average, max, min with appropriate
# labels.
# ------------------------------------------------------------------------------



# this function runs our main objective
def main():
    header() # call the header function

    valList = [] # create empty list


    # initialize variables {counter}
    ctr = 0 
    
    
    
    

    # This function populates the list with values from data file
    fileRead = open('data.txt', 'r')

    for line in fileRead: # initiazlize loop to read data file

        # This section of the for loop keeps track of the count + writes
        # values from data file onto list
        newLine = line.strip('\n')
        value = int(newLine)

        ctr = ctr + 1 # counter
        
        
        valList.append(value)# add the value from the data file to the list

    fileRead.close() # close the data file

    # initialize {max, min, total, avg} AFTER the list has been written to
    avgVal = sum(valList)/len(valList)
    totalVal = sum(valList)
    maxVal = max(valList) 
    minVal = min(valList)

    displayList(valList, ctr, totalVal, avgVal, maxVal, minVal)
    





# This function prints the header of the project
def header():
    print('------------------------------------------------------------------------------')
    print('-------------------------PROJECT 6--------------------------------------------')
    print('----The program displays the count, total, average, max, min with appropriate-')
    print('---------------------------Labels---------------------------------------------')
    print('------------------------------------------------------------------------------')


# gets integer data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")

            

# gets float data from users
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")



# gets string data from users
def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")
    
   


# This fucntion displays the list
def displayList(valList, ctr, totalVal, avgVal, maxVal, minVal):
    print('The list: ',valList)

    print('\n-----RESULT-----')
    print('The COUNT is: ',format(ctr,'.02f'))
    print('The TOTAL value is: ',format(totalVal,'.02f'))
    print('The AVERAGE value is: ',format(avgVal,'.02f'))
    print('The MAXIMUM value is: ',format(maxVal,'.02f'))
    print('The MINIMUM value is: ',format(minVal,'.02f'))
    
    
    
    


    
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






