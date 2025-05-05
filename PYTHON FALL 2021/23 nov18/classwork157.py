# Paul Perez
# NOVEMBER 11 2021
# Classwork 158
# COMPLETED
#---------------------------------------------------------------------------------
# create a template (students). it will have data attribute gradeOne gradeTwo Grade Three
# when objects are created, the name will be populated using a constructor
# we will use a getter to get the name
# print the list of students
# -------------------------------------------------------------------------

# create class
class Student:


    # constructor
    def __init__(self, value1, value2, value3, value4):
        self.name = value1
        self.gradeOne = value2
        self.gradeTwo = value3
        self.gradeThree = value4
        self.average = self.findAvg()


    # method to find the average
    def findAvg(self):
        return(self.gradeOne + self.gradeTwo + self.gradeThree) / 3
        
        
        
    # getter
    def getName(self):
        return self.name

    # getter
    def getGrades(self):
        return self.gradeOne, self.gradeTwo, self.gradeThree


    # getter
    def getAvg(self):
        return self.average
    


   
    
        
    
    
    


# this function runs our main objective
def main():
    header()

    studentList = []



    while(True):
        menu()
        cmd = getStringData('Enter selection: ')
        if(cmd == 'X'):
            print('\nThe list:')

            # iterate the list
            for obj in studentList:
                print('Name:', obj.getName())
                print('Grades: ', obj.getGrades())
                print('Average: ',obj.getAvg())
            
            break
        else:
            print('Adding to list')
            nameStudent = input('Enter the students name: ')
            gradeOne = getFloatData('Enter grade one: ')
            gradeTwo = getFloatData('Enter grade two: ')
            gradeThree = getFloatData('Enter grade three: ')
            myStudent = Student(nameStudent, gradeOne, gradeTwo, gradeThree) # creating an object
            studentList.append(myStudent)# list of object: student











# MENU
def menu():
    print('AllyBaba Learning center')
    print()
    print('A........add a student')
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






