"""
******************************
This program is to demonstrate the syntax of list, including:
- define a list
- search in a 2D list: list of tuples
******************************
Author: Coding Is Fun Junior Team
Date: July 10, 2020
Functions: search the capital city of a country
Version: 1.0
"""
import random


# Search function with parameter list name
# and the country to be searched
def searchCapital(captialList, countryName):
    for i in range(len(captialList)):
        if captialList[i][0].lower() == countryName.lower():
            return captialList[i][1]
    return None


# main function of the program
def main():
    # initializing list of tuples
    # list of capitals
    test_list = [('Canada', 'Ottawa'), ('China', 'Beijing'), ('USA', 'WASHINGTON, D.C.')]

    # printing list
    print("The original list : " + str(test_list))

    # initializing the country name
    # pick a country from list randomly
    tmpNumber = random.randrange(len(test_list))
    countryName = test_list[tmpNumber][0]

    # ask user to guess the capital city
    myAnswer = input("What's the capital city of " + countryName + "? ")

    # Search the capital city of the country
    res = searchCapital(test_list, countryName)

    # Printing result
    if res.lower() == myAnswer.lower():
        print("You are right! " + countryName + " capital city is " + res)
    else:
        print("Opps, it is wrong! " + countryName + " capital city is " + res)


# Runs the program by calling the main() function
if __name__ == '__main__':
    main()