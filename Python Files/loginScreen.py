from userLogin import *

print("______________________________________________________________________________\nHello! And welcome to our program\ Please enter your login information below\n______________________________________________________________________________\n")

createAccount = input("\n Create a new account? (Y/N) \n Exit the login?(E) \n Decision: ")

if(createAccount == "Y"):
    newAccount()
elif (createAccount == "N"):
    existingUser()
elif (createAccount == "E"):
    print("Exiting login")
    quit()
   

# Call viewInventory function
