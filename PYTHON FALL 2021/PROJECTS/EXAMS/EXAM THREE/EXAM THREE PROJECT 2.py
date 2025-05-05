# Paul Perez
# NOVEMBER 19 2021
# EXAM THREE PROJECT
# COMPLETED
#---------------------------------------------------------------------------------
# Validation for Exam grades
# Tests are graded on a 100-point scale with a 10-point bonus question.
# So, a valid test score should be 0 through 110.

# Processing

# Your program should work for any number of students.

# • When the program starts, it should ask the user for the number of students
# to be processed.

# • Function to input the student name/score pairs and store them.

# Input validation:
# the score must be between 0 and 110, inclusive.

# • Function to sort the scores in ascending (increasing) order.

# • Function that calculates the average of the scores.

# • Function that displays a neat table of student name/score pairs
# in sorted order.

# Include appropriate column heading for your table.
# Following the table, display the average score and Letter Grade with appropriate labels.
# ------------------------------------------------------------------------------

# create a class called student
class Student:


    # initialize object attributes
    def __init__(self):
        self.studentName = ''
        self.exam1 = 0
        self.exam2 = 0
        self.exam3 = 0
        self.exam4 = 0
        self.studentAverage = 0




    # getters to retieve obj data attributes from class:Student
    def getStudentName(self):
        return self.studentName

    def getExam1(self):
        return self.exam1

    def getExam2(self):
        return self.exam2

    def getExam3(self):
        return self.exam3

    def getExam4(self):
        return self.exam4

    def getStudentAverage(self):
        return self.studentAverage

        



    # setters to add data attributes to obj in class:Student
    def setStudentName(self,x):
        self.studentName = x

    def setExam1(self,x):
        self.exam1 = x

    def setExam2(self,x):
        self.exam2 = x

    def setExam3(self,x):
        self.exam3 = x

    def setExam4(self,x):
        self.exam4 = x

   





    # function to calculate average of scores
    def calculateAvgerage(self):
        avg = (self.exam1 + self.exam2 + self.exam3 + self.exam4) / 4
        return avg
    


    # function to sort the scores
    def sortScores(self):
        return



    # function displays data
    def displayData(self):
        return
    

    





# this function runs our main objective
def main():
    header() # call the header function


    myList = []

    stuNum = getIntegerData('Enter the number of students: ')
    stuCount = 0


    while(True):
        if(stuNum == stuCount):
            print('\nThe list:')

            # iterate the list
            for obj in myList:
                print('\nName: ', obj.getStudentName().capitalize())
                print('Exam One: ', "{:.2f}".format(obj.getExam1()))
                print('Exam Two: ', "{:.2f}".format(obj.getExam2()))
                print('Exam Three: ', "{:.2f}".format(obj.getExam3()))
                print('Exam Four: ', "{:.2f}".format(obj.getExam4()))
                print('Student Avgerage: ',"{:.2f}".format(obj.calculateAvgerage()))
            break

        else:
            print('\nAdding to list')
            studentName = input('Enter student name: ')
            exam1 = getFloatData('Enter exam one: ')
            exam2 = getFloatData('Enter exam two: ')
            exam3 = getFloatData('Enter exam three: ')
            exam4 = getFloatData('Enter exam four: ')

            myStudent = Student() # creating an object

            # setters to set data 
            myStudent.setStudentName(studentName)
            myStudent.setExam1(exam1)
            myStudent.setExam2(exam2)
            myStudent.setExam3(exam3)
            myStudent.setExam4(exam4)

            myList.append(myStudent)# list of object: student

            stuCount += 1
        
           


    

# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------------EXAM THREE----------------------------')
    print('------------------------Exam grades---------------------------')
    print('--------------------------------------------------------------')    



# this funtion gets INT data from users
def getIntegerData(prompt):
     while (True):
        try:
            value = int(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  Invalid number.  Try again...")



# this function gets FLOAT data from users (POSITIVE ONLY)
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))

            if (0 <= value <= 110):
                return value

            else:
                print('\t\t valid scores are 1-110\n')
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...\n")


# this function will get STRING data 
def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")




main() # first line of execution, it calls function main()
print('\nEnd of Project')






