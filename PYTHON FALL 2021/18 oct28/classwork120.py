# Paul Perez
# OCTOBER 26 2021
# Classwork 120
# COMPLETED
#---------------------------------------------------------------------------------
# # Analyze student grades: name and exam grade
# Menu A for adding - name/grade
# D - display
# X to exit
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    myGrades = {} # empty dictionary








    while (True):
        cmd = getStringData('INPUT: ')



        if (cmd == 'X'):
            print('DONE')
            break


        elif(cmd == 'A'):
            print('ADDING GRADES: ')
            name = input('First Name: ')
            grade = getFloatData('Exam Grade: ')

            # {keys : values}
            # name[key] = value (num,str,string,list,dict)
            myGrades[name] = grade # add to dictionary

        else:
            print('DISPLAY GRADES: ')
            print(myGrades) # display dictionary











        
    
    

        

    
    

    
        


    

    

   






   








# This function creates the menu    
def menu():
    print()
    print('            ==GRADEBOOK FUNCTIONS==')
    print('\t A----- ADD GRADES ')
    print('\t D----- DISPLAY GRADES')
    print('\t X----- EXIT PROGRAM')
    
    



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


# this function will get STRING data from users {commands: A, G, or E}
def getStringData(prompt):
    while (True):
        menu() # call menu
        value = input(prompt)
        value = value.upper()

        if (value in ['A', 'D', 'X']):
            return value
        else:
            print('Invalid entry. try again')




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






