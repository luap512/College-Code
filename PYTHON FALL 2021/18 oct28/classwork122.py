# Paul Perez
# OCTOBER 26 2021
# Classwork 120
# COMPLETED
#---------------------------------------------------------------------------------
# Buger Joint
# B to buy: tells what burger type and the price
# D to display my order
# T to exit and print the total bill
#
# ask the user to enter tax rate and find the tax amount and the total due
# -------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    myOrder = {} # empty dictionary


    





    while (True):
        cmd = getStringData('INPUT: ')



        if (cmd == 'T'):
            print('DONE')
            findTotalCost(myOrder)
            break


        elif(cmd == 'B'):
            print('ORDER: ')
            burger = input('burger: ')
            price = getFloatData('price: $')
            

            # {keys : values}
            # name[key] = value (num,str,string,list,dict)
            myOrder[burger] = price # add to dictionary

        else:
            print('DISPLAY ORDER: ')
            print(myOrder) # display dictionary











        
    
    

        

    
    

    
        


    

    

   



# This function finds the total cost
def findTotalCost(myOrder):

    total = 0

    for order in myOrder:
        total = total + myOrder[order]

    print('total is $' + format(total,'.02f'))

    tax = findTaxCost(total)
    totalCost = total + tax
    print('Tax is: $' , format(tax,'.02f'))
    print('Total cost is: $', format(totalCost,'.02f'))


def findTaxCost(total):

    taxPercentage = getFloatData('Tax percentage: %')
    taxCost = total * (taxPercentage / 100)
    return taxCost
    

    
    
    
   








# This function creates the menu    
def menu():
    print()
    print('            ==DINING FUNCTIONS==')
    print('\t B----- BUY FOOD ')
    print('\t D----- DISPLAY ORDER')
    print('\t T----- PAY AND EXIT')
    
    



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
        menu() # call menu
        value = input(prompt)
        value = value.upper()

        if (value in ['B', 'D', 'T']):
            return value
        else:
            print('Invalid entry. try again')




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






