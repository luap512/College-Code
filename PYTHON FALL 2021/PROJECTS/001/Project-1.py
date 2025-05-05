# Paul Perez
# September 9 2021
# Project 1
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Enter 2 integers, find and display the sum. difference product and
# modulus
# ------------------------------------------------------------------------------
def main():
    print('PROJECT ONE\n')

    # getting data from users
    numberOne = int(input('Enter the first number: '))
    numberTwo = int(input('Enter the second number: '))
    

    #calculate the sum, modulus. difference. and product.
    sumNum = numberOne + numberTwo
    difNum = numberOne - numberTwo
    modNum = numberOne % numberTwo
    prodNum = numberOne * numberTwo


    #Display results
    print('The first number is: ',numberOne,)
    print('The second number is: ',numberTwo,)
    print('The sum of the two numbers is: ',sumNum,)
    print('The difference between the two numbers is: ',difNum,)
    print('The product of the two numbers is: ',prodNum,)
    print('The modulus of the two numbers is: ',modNum,)
    
    
    
main()
print('\nEnd of Project')




