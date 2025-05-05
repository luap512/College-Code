# Paul Perez
# NOVEMBER 11 2021
# Classwork 161
# COMPLETED
#---------------------------------------------------------------------------------

# -------------------------------------------------------------------------

# create class
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
    menuList = []

    taxRate = getTaxRate()
    loadMenu(menuList)

    while(True):
        cmd = menu() # O,E

        if(cmd == 'O'):
            while(True):
                choice = displayItems(menuList)
                if (choice == 'X'):
                    print('Cancelling the order')
                    break
                elif(choice == 'T'):
                    print('Totalling the order')
                    break
                else:
                    print(menuList[int(choice) - 1].getItem())

        else:
            print('Exiting POS')
            break

    


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
    print('\tO Start a new order')
    print('\tX Exit point of sale')
    print('----------------------------------------')


    while(True):
        cmd = input('Enter your choice: ')
        cmd = cmd.upper()

        if(cmd == 'X'):
            return cmd

        elif(cmd == 'T'):
            print('Totalling the order')
            return cmd

        elif(cmd >= '1' and cmd <= str(count)):
            print('Ordering somehting')
            return cmd
        else:
            print('Oops wrong entry')




def menu():
    print('ALLYBABA EMPLOYEE CENTER')
    print()
    print('O start a new order')
    print('E end of shift')
    print()

    while(True):
        cmd = input('Enter your selection')
        cmd = cmd.upper()
        if (cmd in ['O','E']):
            return cmd
        else:
            print('Wrong entry')
            
            
        

        



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






