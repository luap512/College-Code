# Paul Perez
# NOVEMBER 8 2021
# Project 10 
# COMPLETED
#---------------------------------------------------------------------------------
# Write a program that will be a Point of Sale system at a food stall.
# The list of items and corresponding prices will be loaded from a text file.
# Also, the sales tax will be loaded from a text file.

# The Menu lists all the items and the following 3 commands.  
# X = cancel the sale and start over
# T = total the sale.
# E = close the shift

# The program repeatedly displays the Menu until the shift is closed (E is entered). 
# The program keeps a running total of the amount of sales and the end of
# shift the total sales is displayed. Only one item is ordered at a time

# When “X” is entered,
# It clears the running totals and displays the Menu again. 

# When “T” is entered,
# It displays the items purchased, the total price before sales tax. the sales tax due
# and the final total including the tax. 

# When “E” is entered,
# the program exits.  It displays how many each item sold, the sub-total,
# the total sales tax, and the grand total.

# Your numeric output is formatted to show two decimal places.
# -------------------------------------------------------------------------------------


# create class menu. Items on menu are objects
class Menu:
    def __init__ (self, item, price):
        self.item = item
        self.price = price


        # getter
    def getItem(self):
        return self.item

    def getPrice(self):
        return self.price

        


# this function runs our main objective
def main():

    menuList = [] # List of menu items(objects) on the menu(class)
    orderList = [] # list of order (one per customer)
    orderCost = 0
    totalSales = 0 
    totalOrders = 0

    taxRate = getTaxRate()
    loadMenu(menuList)

    while(True):
        cmd = menu() # O,E

        if(cmd == 'O'):
            while(True):
                choice = displayItems(menuList)
                if (choice == 'X'):
                    orderCost = 0
                    print('----------------------')
                    print('Cancelling the order\n')
                    
                
                elif(choice == 'T'):
                    totalSales += orderCost
                    totalOrders += 1
                    print('----------------------')
                    print('Totalling the order:')
                    print(orderList)
                    print('Subtotal: $',orderCost)
                    print('Tax: %',getTaxRate())
                    print('total: $',"{:.2f}".format(orderCost * (getTaxRate())/100 + orderCost),'\n')
                    orderCost = 0
                    orderList = []
                    

                elif(choice == 'E'):
                    print('----------------------')
                    print('Exiting shift')
                    print('Total orders for this shift: ',totalOrders)
                    print('Total sales for this shift: $',totalSales)
                    break
                    
                else:
                    orderList.append(menuList[int(choice) - 1].getItem())
                    orderCost += menuList[int(choice) - 1].getPrice()
                    print('\t',menuList[int(choice) - 1].getItem(),'$',menuList[int(choice) - 1].getPrice(),'\n')



        else:
            print('\n\tCLOCKING OUT NICE WORK')
            break

    

# function adds each item(objects) on the menu(class) to the list menuList
def loadMenu(menuList):
    fileRead = open('menu.txt','r')
    

    for line in fileRead:

        line = line.strip('\n')
        mList = line.split(',')
        item = mList[0]
        price = float(mList[1])
        itemObj = Menu(item,price) # create object for each item
        menuList.append(itemObj)

    fileRead.close()
    

# returns tax rate from file
def getTaxRate():
    fileRead = open('tax.txt','r')

    line = fileRead.readline()
    taxRate = float(line)

    fileRead.close()

    return taxRate



# displays all items
def displayItems(menuList):
    count = 1
    for obj in menuList:
        print(count, obj.getItem(), '\t', obj.getPrice())
        count += 1
    print('----------------------------------------')
    print('\tX CANCEL <=')
    print('\tT TOTAL <=')
    print('\tE EXIT <=')
    print('----------------------------------------')


    while(True):
        cmd = input('Enter your choice: ')
        cmd = cmd.upper()

        if(cmd == 'X'):
            print('\tCancelling order...\n')
            return cmd

        elif(cmd == 'T'):
            print('\tTotaling order...\n')
            return cmd

        elif(cmd == 'E'):
            print('\tExiting...\n')
            return cmd


        elif(cmd >= '1' and cmd <= str(count)):
            print('\tAdded to order: ')
            return cmd

        else:
            cmd = input('Enter your choice: ')
            print('\tOops wrong entry...\n')




def menu(): # O,E
    print('ALLYBABA EMPLOYEE CENTER')
    print('------------------------')
    print('O - CLOCK IN')
    print('E - CLOCK OUT')
    print('-------------------------')

    while(True):
        cmd = input('Enter your selection: '+'\n')
        cmd = cmd.upper()
        if (cmd in ['O','E']):
            return cmd
        else:
            print('Wrong entry')
            
            
        

        



    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------PROJECT 10----------------------------------')
    print('----FOOD VENDOR-----------------------------------------------')
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






