# Paul Perez
# NOVEMBER 11 2021
# Classwork 134
# COMPLETED
#---------------------------------------------------------------------------------
#Class
# -------------------------------------------------------------------------


class Employees:
    # data members(attributes)
    name = 'paul'
    dob = '01/01/2020'
    ssn = '123-45-6547'



# this function runs our main objective
def main():
    paul = Employees() #add paul to the class. paul is now an object
    print(paul.name)
    print(paul.dob)
    print(paul.ssn)
    

    
    



    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 120------------------------------')
    print('----WALLSTREET VIBES M80--------------------------------------')
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




# this function gets FLOAT data from users (POSITIVE ONLY)
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (value >= 0):
                return value

            else:
                print('\t\t grade must be greater than zero')
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")


# this function will get STRING data from users {commands: B, D, or T}
def getStringData(prompt):
    value = input(prompt)
    value = value.upper()
    return value
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






