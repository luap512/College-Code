# Paul Perez
# NOVEMBER 9 2021
# Classwork 129
# COMPLETED
#---------------------------------------------------------------------------------
# a = 5, b = 6, c = 6, 
# write a calculate function that will return the sum of the three numbers
# write a print function that will print the result
# -------------------------------------------------------------------------
# Trace 93-14-15-16-17-19-24--26-19-21-32--33-94


# this function runs our main objective
def main():
    a = 5
    b = 6
    c = 6

    total = calculate(a, b, c)

    display(total)

# function calculates sum of three nums
def calculate(a, b, c):
        total = a + b + c
        return total
    
    


# function displays results
def display(total):
    print('The sum is: ',total)

    
    



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






