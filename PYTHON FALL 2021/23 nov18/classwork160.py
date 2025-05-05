# Paul Perez
# NOVEMBER 11 2021
# Classwork 161
# COMPLETED
#---------------------------------------------------------------------------------
# Template: student
# data attributes: name, wage, hours worked
# constructor creates object
# setter populates data attributes
# -------------------------------------------------------------------------

# create class
class Employee:


    # constructor
    def __init__(self):
        self.name = ''
        self.wage = 0
        self.hrsWorked = 0
        

    # fucntion to find gross pay
    def calcGrossPay(self):
        if(self.hrsWorked > 40):
            overTime = self.hrsWorked - 40
            grossPay = 40 * self.wage + overTime * self.wage * 1.5
        else:
            grossPay = self.hrsWorked * self.wage

        return grossPay






   # setters (set values for attributes)
    def setName(self,value):
        self.name = value

    def setWage(self,value):
        self.wage = value

    def setHrsWorked(self,value):
        self.hrsWorked = value




    # getters (retrieve values)
    def getName(self):
        return self.name

    def getWage(self):
        return self.wage

    def getHrsWorked(self):
        return self.hrsWorked
   
    
        
    
    
    


# this function runs our main objective
def main():
    header()

    myList = []



    while(True):
        menu()
        cmd = getStringData('Enter selection: ')
        if(cmd == 'X'):
            print('\nThe list:')

            # iterate the list
            for obj in myList:
                print('\nName:', obj.getName())
                print('Wage:', obj.getWage())
                print('Hours:', obj.getHrsWorked())
                print('Gross pay: ',obj.calcGrossPay())
            break

        else:
            print('Adding to list')
            employeeName = input('Enter emplpoyee name: ')
            employeeWage = getFloatData('Enter wage: ')
            employeeHrs = getFloatData('Enter hours worked: ')

            myEmployee = Employee() # creating an object

            # setters to set data 
            myEmployee.setName(employeeName)
            myEmployee.setWage(employeeWage)
            myEmployee.setHrsWorked(employeeHrs)

            myList.append(myEmployee)# list of object: student











# MENU
def menu():
    print('\nLIST OF EMPLOYEES')
    print()
    print('A........add employee')
    print('X........exit and print')



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


# this function will get STRING data from users {commands: X OR A}
def getStringData(prompt):
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in ['A', 'X']):
            return value.capitalize()
        else:
            print ('\t\t Opps! Wrong entry')
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






