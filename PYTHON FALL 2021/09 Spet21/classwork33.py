# Paul Perez
# September 16 2021
# Classwork 33
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: program will calculate sales tax
# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function



    # Getting sales value and tax rate from user
    salesAmmount = getFloatData('enter the cost of your purchase: $')
    taxRate = getFloatData('enter the sales tax rate: %')
    
   
    
    
    # Calculate grade
    taxAmmount, totalSales = doCalculate(taxRate, salesAmmount)




    # call display function
    displayResult(salesAmmount, taxAmmount, totalSales)


    




# This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------class work 33-------------------------------')
    print('----user enters sales and tax rate program displays price-----')
    print('--------------------------------------------------------------')
    

# This function displays the results    
def displayResult(salesAmmount, taxAmmount, totalSales):
    print('\nResult')
    print('the sales ammount: ', format(salesAmmount, '.02f'))
    print('the tax ammount: ', format(taxAmmount, '.02f'))
    print('the total ammount: ', format(totalSales, '.02f'))

# This fucntion calculates the taxAmmount and total Sales
def doCalculate(taxRate, salesAmmount):
    taxAmmount = (salesAmmount * (taxRate/100))
    totalSales = salesAmmount + taxAmmount
    return taxAmmount, totalSales  
    


# this funtion gets Integer data from users
def getFloatData(prompt):
    value = float(input(prompt))
    return value

main() # first line of execution, it calls function main()
print('\nEnd of Project')






