# Paul Perez
# NOVEMBER 19 2021
# EXAM THREE PROJECT
# COMPLETED
#---------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# create a class called student
class Student:


    # initialize object attributes
    def __init__(self):
        self.studentNum = 0
        self.studentName = ''
        self.exam1 = 0
        self.exam2 = 0
        self.exam3 = 0
        self.exam4 = 0




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

    def getStudentNum(self):
        return self.studentNum
        



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

    def setStudentNum(self,x):
        self.studentNum = x




    # function to calculate average of scores
    def calculateAvgerage(self):
        return

    # function to sort the scores
    def sortScores(self):
        return

    # function displays data
    def displayData(self):
        return
    

    





# this function runs our main objective
def main():
    header() # call the header function

    studentList = [] # create list of students

    studentCount = 0
    totalStudents = getIntegerData('How many students: ')# get number of students

    while (True):
        if(studentCount < totalStudents):

            studentCount += 1 # count students
            studentName = getStringData('\nEnter student name: ')
            exam1 = getFloatData('Enter exam one grade: ')
            exam2 = getFloatData('Enter exam two grade: ')
            exam3 = getFloatData('Enter exam three grade: ')
            exam4 = getFloatData('Enter exam four grade: ')

            objStudent = Student() # create object in class student

            # set attributes for  student object
            objStudent.setStudentNum(studentCount)
            objStudent.setExam1(exam1)
            objStudent.setExam2(exam2)
            objStudent.setExam3(exam3)
            objStudent.setExam4(exam4)

            # add object to list
            studentList.append(objStudent)

        else:
            for obj in studentList:
                print('\n')
                print('Student Number:', objStudent.getStudentNum())
                print('Student Name:', objStudent.getStudentName())
                print('Exam One Grade:', objStudent.getExam1())
                print('Exam Two Grade:', objStudent.getExam2())
                print('Exam Three Grade: ',objStudent.getExam3())
                print('Exam Four Grade: ',objStudent.getExam4())
                print('Average:')
            break
            

        
        
           

    


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

            if (value >= 0):
                return value

            else:
                print('\t\t No negative values...try again.\n')
            
                
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






