# Paul Perez
# September 16 2021
# Classwork 29
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will find my letter grade
# 90+   A
# 80-90 B
# 70-80 C
# 60-70 D
# 1-60  F
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Get value from users
    myGrade = float(input('Enter your grade: '))
   
    
    

    print('\nResults')
    # Calculate grade
    if (myGrade >= 90):
              print('Your grade is A')
    elif(myGrade >= 80):
            print('Your grade is B')
    elif (myGrade >= 70):
            print('Your grade is C')
    elif (myGrade >= 60):
            print('Your grade is D')
    else:
            print('Your grade is F')




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 29-------------------------------')
    print('gets your age and cash on hand and determines if you can party')
    print('--------------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






