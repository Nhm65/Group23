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

    inBase = "SELECT password FROM users WHERE username = Username"

    if Username in inBase:
        print("\n Your account username exists \n")
    elif newUsername in inBase:
        print("\n Your newly created username exists \n")

    if Password in inBase:
        print("\n Your account Password exists \n")   
    elif newPassword in inBase:
        print("\n Your new password exists \n")

    #call functions in view Inventory if database clears
    print("\n Calling view inventory \n")

    displayMenu()
    menuChoice()









    

