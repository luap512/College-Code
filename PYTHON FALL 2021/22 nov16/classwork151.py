# Paul Perez
# NOVEMBER 11 2021
# Classwork 154
# COMPLETED
#---------------------------------------------------------------------------------
# create a template (students). it will have name and age as data attribute
# when objects are created, the name will be populated using a constructor
# we will use a getter to get the name
# -------------------------------------------------------------------------

# create class
class Student:


    # constructor
    def __init__(self, value1, value2):
        self.name = value1
        self.age = value2
        
        
    # getter
    def getName(self):
       return self.name

    def getAge(self):
        return self.age

   
    
        
    
    
    


# this function runs our main objective
def main():

    studentName = input('Enter your name: ')
    studentAge = getIntegerData('Enter your age: ')
    myStudent = Student(studentName, studentAge) # object is created
    print('The student: ', myStudent.getName())
    print('The student: ', myStudent.getAge())



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
    while (True):
        value = input(prompt)
        value = value.upper()

        if (value in ['MALE', 'FEMALE']):
            return value.capitalize()
        else:
            print ('\t\t Opps! Wrong entry')
       




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






