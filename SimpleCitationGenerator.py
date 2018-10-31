# Made by Lucien Hammond

import sys

exit = 0

while exit != 1:
    print("Supported Citations: APA and MLA")
    decidingCitation = input("Enter name of citation: ")

    if decidingCitation == "APA":
        Firstname = input("Enter First name of author: ")
        Lastname = input("Enter last name of author: ")
        Title = input("Enter the title of the website: ")
        URL = input("Enter the URL here: ")
        Month = input("Enter the month here(Number): ")
        Day = input("Enter the day here: ")
        Year = input("Enter the year here(last 2 digits): ")

        print(Lastname + ", " + Firstname + ", " + Title + "." + "[Online] " + URL + ", Accessed: " + Month + "/" + Day + "/" + Year + ".")
        enter = input('Hit enter to continue...')

    if decidingCitation == "MLA":
        Firstname = input("Enter First name of author: ")
        Lastname = input("Enter last name of author: ")
        Websitename = input("Enter the name of the website: ")
        Title = input("Enter the title of the website: ")
        URL = input("Enter the URL here: ")
        Month = input("Enter the month here(First 3 letters): ")
        Day = input("Enter the day here: ")
        Year = input("Enter the year here: ")
        Publisher = input("Enter the name of the publisher: ")

        print(Lastname + ", " + Firstname + ". " + '"' + Title + '." ' + Websitename + '(you need to italicize this)' + ', ' + Publisher + ', ' + Day + " " + Month + ". " + Year + ", " + URL + ".")

        enter = input('Hit enter to continue...')

    if decidingCitation == "exit":
        sys.exit()
    