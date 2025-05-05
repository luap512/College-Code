# Paul Perez
# September 9 2021
# Project 2
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: The user enters the sales amount.
# The user enters the sales tax rate (use decimals)
# The program finds the tax amount and the total amount with
# the sales tax amount.
# The program displays the sales amount, the tax amount and total
# amount with appropriate labels and formatted 2 decimal places.
# Make sure to use main(), and few more functions
# ------------------------------------------------------------------------------
def main():
    header()

    # retrieving data from users
    saleCost = float(input('Enter the total cost of your items: $'))
    saleTax = float(input('Enter the sales tax: %'))
    

    # calculate the taxes paid and the total cost
    taxCost = (saleTax/100) * saleCost
    totalCost = taxCost + saleCost
    


    # Display results
    displayResults(taxCost, totalCost, saleCost)
    






def header(): # function to display header
    print('-------------------------------------------------------------------')
    print('------------------Project TWO--------------------------------------')
    print('Program determines the total cost of a purchase including sales tax')
    print('-------------------------------------------------------------------')


def displayResults(taxCost, totalCost, saleCost): # Function to display results
    print('\nResult:')
    print('\nyour items cost $',format(saleCost,'.02f'), '\nyour tax cost is $',format(taxCost,'.02f'),'\nyour total cost is $',format(totalCost, '.02f'))
    
    
    
main()
print('\nEnd of Project')




