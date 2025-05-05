# Paul Perez
# OCTOBER 19 2021
# Classwork 90
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Users will enter grades until a negative is entered
# find the average and count how many are over average
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    gradeList = []
    populateList(gradeList)
    
    

    counter = len(gradeList)
   
    sumNum = sum(gradeList)
    numAvg = sumNum / counter
    
    countOverAverage = 0

    for ctr in gradeList:
        if(ctr > numAvg):
            countOverAverage = countOverAverage + 1
    print('The count over average is: ',countOverAverage)
       

    
        


    

    

   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 80-------------------------------')
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
    while (True):
        try:
            value = float(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")




def populateList(gradeList):
    value = getIntegerData('Enter Grades: <negative value will terminate>')
    while(value >= 0):
        gradeList.append(value)
        value = getIntegerData('Enter Grades: <negative value will terminate>')
        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






