# Paul Perez
# September 9 2021
# Classwork 18
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Users enter base and height (float) of triangle.
# Program will find and display the area of a triangle
# ------------------------------------------------------------------------------
def main():
    print('Classwork 18\n')

    # getting data from users
    triangleBase = float(input('Enter the base of the triangle: '))
    triangleHeight = float(input('Enter the height of the triangle: '))
    

    #calculate the area of the triangle.
    triangleArea = ((triangleBase * triangleHeight)//2)


    #Display results
    print('\nThe base of the Triangle is: ',triangleBase,)
    print('The height of the Triangle is: ',triangleHeight,)
    print('Therefore, the area of the Triangle is: ',triangleArea,)
    
    
    
main()
print('\nEnd of Project')




