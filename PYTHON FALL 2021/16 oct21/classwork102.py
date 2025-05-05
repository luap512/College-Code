# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: list, tuples, strings    -slicing

# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    numberList =[23, 45, 67, 90, 99, 12, 11, 3, 5]
    
            
    # slicing the data set
    print('my List: ',numberList)
    print('first element: ',numberList[0] )
    print('last element: ',numberList[-1] )
    print('from second element to the end: ',numberList[1:])
    print('from fifth element to the end: ',numberList[4:])
    print('all elements up to the fifth element: ',numberList[:4])
    print('all elements before the last element: ',numberList[:-1])
    print('all elements second to fifth: ',numberList[1:5])
    print('all elements third to seventh: ',numberList[2:7])
    
   


  
    

    
    

    
        


    

    

   






   








    
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






