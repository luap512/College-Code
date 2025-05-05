# Paul Perez
# NOVEMBER 11 2021
# Classwork 134
# COMPLETED
#---------------------------------------------------------------------------------
#Class
# -------------------------------------------------------------------------

# create class
class KBAllyHomes:
    # data members(attributes)
    model = '2340'
    bedRoom = 5
    bathRoom = 5
    address = ''



# this function runs our main objective
def main():
    micheleHouse = KBAllyHomes() # objects
    paul = KBAllyHomes()
    shelby = KBAllyHomes()

    micheleHouse.address = '101 ally lane'
    paul.address = '999 baba lane'
    shelby.address = '123 ally babab street'

    paul.bedRoom = 10
    shelby.bathRoom = 1

    print(shelby.address)
    
    

    
    



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






