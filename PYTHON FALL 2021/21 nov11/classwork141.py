# Paul Perez
# NOVEMBER 11 2021
# Classwork 142
# COMPLETED
#---------------------------------------------------------------------------------
# create a class Employee. 3 attributes: name, hours worked, hourly wage
# (allybaba, 50hrs, 10/hr)
# method that will print the gross pay
# create an object and print the gross pay
# -------------------------------------------------------------------------

# create class
class Employee:
    name = 'allybaba'
    hrsWorked = 50
    hrsWage = 10

    

    def printMe(self): # need to use self
        if(self.hrsWorked > 40):
            grossPay = 40 * self.hrsWage + (self.hrsWorked - 40) * self.hrsWage * 1.5
        else:
            grossPay = hrsWorked * hrsWage

        print('gross pay is: ',grossPay)


# this function runs our main objective
def main():

    myEmployee = Employee()
    name = input('Enter employee name: ')
    wage = getFloatData('Enter the age: ')
    hours = getFloatData('Enter the hours: ')
    myEmployee.name = name
    myEmployee.hrsWorked = hours
    myEmployee.hrsWage = wage
    myEmployee.printMe()

    
    



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






