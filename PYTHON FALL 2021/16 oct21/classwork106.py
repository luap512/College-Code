# Paul Perez
# OCTOBER 19 2021
# Classwork 91
# COMPLETED
#---------------------------------------------------------------------------------
# Goal: Tcheck how many vowels are in the sentence

# ------------------------------------------------------------------------------
# Trace


# this function runs our main objective
def main():
    header() # call the header function

    sentence = "AlyyBaba coin is the future of my pocket where i will enhance my spiritual richness"
    sentence = sentence.upper()
    vowels = ['a', 'e', 'i', 'o', 'u']
    countVowels = 0

    for vw in vowels:
        countVowels = countVowels + sentence.count(vw.upper())

    print('Count vowels: ', countVowels)
            
    
       


  
    

    
    

    
        


    

    

   






   








    
    # This function prints the header of the project
def header():
    print('--------------------------------------------------------------')
    print('------------------CLASS WORK 80-------------------------------')
    print('----REVIEW----------------------------------------------------')
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




# this function gets FLOAT data from users
def getFloatData(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value
            
                
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")



def getStringData(prompt):
    while (True):
        try:
            value = str(input(prompt))
            return value
            
                
        except ValueError:
            print("Invalid input  Try again...")




        
    

main() # first line of execution, it calls function main()
print('\nEnd of Project')






