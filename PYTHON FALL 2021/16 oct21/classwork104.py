# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: TUPLES (defined by parenthesis) tuples cannot be altered

# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    myTuple = (12, 45, 67, 8, 9, 89, 678, 567, 678, 667, 999, 1000)
    
            
    # slicing the data set
    print('sentence: ',myTuple)
    print('first element: ',myTuple[0])
    print('first element: ',myTuple[-1])
    print('second element to the last: ',myTuple[1:])
    print('3rd element to the 7th: ',myTuple[2:7])
       


  
    

    
    

    
        


    

    

   






   








    
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



def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






