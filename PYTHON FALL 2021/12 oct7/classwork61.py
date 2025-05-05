# Paul Perez
# September 28 2021
# Classwork 60
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: find The letter grade for each new numeric grade
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    
    


    fileRead = open('textDoc1.txt', 'r') # file read is an object that points to textdoc1
    for line in fileRead:
        newLine = line.strip('\n') #removing end of line marker
        value = int(newLine)  #converting string to integer
        print(value)
        letterGrade = getLetterGrade(value)
        print('The letter grade is: ',letterGrade)


    
    fileRead.close()
    




   

def getLetterGrade(value):
    # Checking the values
        if (value >= 90):
            return 'A'
        elif(value >= 80):
            return 'B'
        elif(value >= 70):
            return 'C'
        elif(value >= 60):
            return 'D'
        else:
            return 'F'






    
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






