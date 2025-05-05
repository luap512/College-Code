# Paul Perez
# September 27 2021
# EXAM ONE
# COMPLETED
#---------------------------------------------------------------------------------
# Write a program that will manage the income flow for AllyBaba Rental property
#
# AllyBaba owns a house. The house is 1,000 sq. ft. with 1 bedroom and 1 full
# bathroom. The rent is $1,000 per month. There are additional monthly fees for the
# rental. The additional monthly fees are:
# • Trash
# • Water
#
# 1. If the rent is paid on or before the 3rd of the month, there will be no late fees.
# • lateFees = 0
# 2. If the rent is paid after the 3rd day of the month, there will be $5.00 late fees
# for each day being late after the 3rd.
# • If the rent pay day is 4, lateFees = (4 – 3) * 5 = 5
# 3. If the rent pay day after 30th, there will be a one-time fixed payment of $7
# • lateFees = 700
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function


# call the fucntion gets user data
    print('\n----USER INPUTS----')
    year = getStringData('Enter the year: ')
    month = getStringData('Enter the month: ')
    monthDay = getIntegerData('Enter the day of the month: ')
    trashAmount = getFloatData('Enter the fee for trash: $')
    waterAmount = getFloatData('Enter the fee for water: $')
    

# if/else tree to determine the late fees based on days late
    if(monthDay >30):
        lateFees = 700
        daysLate = doCalculateDays(monthDay)
    else:
        lateFees = doCalculateDays(monthDay) * doCalculateFees(monthDay)
        daysLate = doCalculateDays(monthDay)



# call the total cost function
    totalCost = doCalculateCost(lateFees, waterAmount, trashAmount)



# call the display results function
    displayResult(month, monthDay, trashAmount, waterAmount, lateFees, daysLate, totalCost, year)
     

    
# This function prints the header of the project
def header():
    print('-----------------------------------------------------------------------------')
    print('------------------EXAM ONE---------------------------------------------------')
    print('Write a program that will manage the income flow for AllyBaba Rental property')
    print('-----------------------------------------------------------------------------')
    print('-----------------------------------------------------------------------------')
        


# this funtion gets Integer data from users
def getIntegerData(prompt):
    value = int(input(prompt))
    return value


# this function gets string data from users
def getStringData(prompt):
    value = str(input(prompt))
    return value

#this function gets Float data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value



# this function calculates how many days late the rent was
def doCalculateDays(monthDay):
    value = (monthDay - 3)
    return value


# this function calculates which late fee will be applied 
def doCalculateFees(monthDay):
    if(monthDay <= 3):
       return 0
    elif(monthDay <= 30):
        return 5
    elif(monthDay > 30):
        return 700


# this function calculates the total cost
def doCalculateCost(lateFees, waterAmount, trashAmount):
    cost = 1000 + lateFees + waterAmount + trashAmount
    return cost

    

# display 
def displayResult(month, monthDay, trashAmount, waterAmount, lateFees, daysLate, totalCost, year):
    print('\n')
    print('----RESULTS-----')
    print('=======RENTAL TRANSACTION FOR',month,year,'=======' )
    print('Monthly rent:                     $ 1000')
    print('Trash Charges:                    $',trashAmount)
    print('Water Charges:                    $',waterAmount)
    print('Late fees: (',  daysLate,'x $5)             $',lateFees)
    print('\nTotal due:'                              '$',"{:0.2f}".format(totalCost))
    



main() # calls function main()
print('\nEnd of Project')






