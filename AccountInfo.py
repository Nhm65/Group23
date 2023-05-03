from ssl import _PasswordType


def UserIDedit():
    print("--What would you like to change? Select the number of your option.--\n")
    print("-1. Create UserID-\n")
    print("-2. Edit Personal Information-\n")
    return UserIDedit

def UserIDCreate():
    username = input("Make your username/name here: \n")
    password = input("Make your password here; make sure it isn't something an 8-year-old can guess. \n")
    print("Alright! You have a new account now. /n")
    return UserIDCreate

def AddressChange():
    print("What is your new address? (Put N/A if not applicable) \n")
    address = input("Address \n")
    city = input("City \n")
    state = input("State \n")
    zip_code = input("Zip Code \n")
    print("New Address Updated")
    return AddressChange

def deleteUserID():
    del username
    del password
    del address
    del city
    del state
    del zip_code
    return deleteUserID
    

def UserIDeditChoice():
    choice = input("\n Choice: ")
    if (choice == 1):
        UserIDCreate()
    if (choice == 2):
        AddressChange()
    if (choice == 3):
        deleteUserID()
        return UserIDeditChoice




