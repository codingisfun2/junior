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


# Search function with parameter list name
# and the country to be searched
def searchCapital(captialList, countryName):
    for i in range(len(captialList)):
        if captialList[i][0].lower() == countryName.lower():
            return captialList[i][1]
    return "Sorry, I don't know."


# main function of the program
def main():
    # initializing list of tuples
    # list of capitals
    test_list = [('Canada', 'Ottawa'), ('China', 'Beijing'), ('USA', 'WASHINGTON, D.C.')]

    # printing list
    print("The original list : " + str(test_list))

    # initializing the country name
    # ask user to enter country name
    myCountry = input("Please entry the country name: ")

    # Search the capital city of the country
    res = searchCapital(test_list, myCountry)

    # Printing result
    print(myCountry + " capital city is " + res)

# Runs the program by calling the main() function
if __name__ == '__main__':
    main()