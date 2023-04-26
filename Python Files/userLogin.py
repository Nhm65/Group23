from ViewInventory import *
from insertNewUser import *

# Test base
#userNameUpdate = ["Nick"]
#passwordUpdate =  ["Manning"]

def newAccount(): 
    userCreat()

    #call existing user
    existingUser()

#For existing user, figure out how to compare the database to see if the username and password exist

def existingUser():
    Username = input("\n Username: ")
    Password = input("\n Password: ")

    if Username in userNameUpdate:
        print("\n Your account username exists \n")
    elif newUsername in userNameUpdate:
        print("\n Your newly created username exists \n")

    if Password in passwordUpdate:
        print("\n Your account Password exists \n")
    elif newPassword in passwordUpdate:
        print("\n Your new password exists \n")

    #call functions in view Inventory if database clears
    print("\n Calling view inventory \n")

    displayMenu()
    menuChoice()









    

