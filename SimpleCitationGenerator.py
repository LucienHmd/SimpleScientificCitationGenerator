# Made by Lucien Hammond

import sys

exit = 0
print("Supported Citations: APA")
while exit != 1:
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
    if decidingCitation == "MLA":
        
    if decidingCitation == "exit":
        sys.exit()
    