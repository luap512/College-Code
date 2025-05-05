# Paul Perez
# September 14 2021
# Classwork 25
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Program will get age data from users (integer a) and cash in pocket(float)
# display 'you can partyyyy' if age is over 21 and money is greater thatn 10000
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    # Get value from users
    ageVal = int(input('Enter your age: '))
    moneyVal = float(input('Enter your net worth: '))


    # Display result if more than 10
    if (ageVal >= 21):
              if (moneyVal >= 10000):
                  print('you can partyyyyy! be safe though!')
    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 25-------------------------------')
    print('gets your age and cash on hand and determines if you can party')
    print('--------------------------------------------------------------')
    

    
    


main() # first line of execution, it calls function main()
print('\nEnd of Project')






