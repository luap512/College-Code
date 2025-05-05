# Paul Perez
# OCTOBER 12 2021
# Classwork 70
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: make a loop from 1 to 10 using for loop
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    fileWrite = open('output.txt', 'w')
        

    for counter in range(1,22):
        fileWrite.write(str(counter) + '\n')

    fileWrite.close()   
        


   






   








    
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






