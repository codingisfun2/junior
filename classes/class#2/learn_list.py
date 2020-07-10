"""
******************************
This program is to demonstrate the syntax of a list of tuples
******************************
Author: Coding Is Fun Junior Team
Date: July 10, 2020
Functions: define a list of tuples and get value by index
Version: 1.0
"""
import random


# main function of the program
def main():
    # initializing list of tuples
    # list of capitals
    test_list = [('Canada', 'Ottawa'), ('China', 'Beijing'), ('USA', 'WASHINGTON, D.C.')]

    # printing list
    print("The original list : " + str(test_list))

    # pick a country from list randomly
    tmpNumber = random.randrange(len(test_list))
    # get country name
    myCountry = test_list[tmpNumber][0]
    myCapital = test_list[tmpNumber][1]

    # Printing capital city
    print(myCountry + " capital city is " + myCapital)

# Runs the program by calling the main() function
if __name__ == '__main__':
    main()