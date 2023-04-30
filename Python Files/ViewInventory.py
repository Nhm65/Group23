def displayMenu():
    print("\n Welcome to the inventory \n ")
    print("______________________________________________________________________________________")
    print("____                             BILL'S TACKLE SHOP                               ____")
    print("____                                                                              ____")
    print("____  1. Tackle                                                                   ____")
    print("____  2. Rods                                                                     ____")
    print("____  2. Reels                                                                    ____")
    print("____  2. Clothing                                                                 ____")
    print("____                                                                              ____")
    print("______________________________________________________________________________________")

def displayTackle():
    print("______________________________________________________________________________________")
    print("____                             Tackle                                           ____")
    print("____                                                                              ____")
    print("____  1. Megabass Jerkbait             Price: (25.00)                             ____")
    print("____  2. Kvd Squarebill                Price: (7.50)                              ____")
    print("____  2. Alabama rig                   Price: (20.00)                             ____")
    print("____  2. Zoom Lizard                   Price: (3.50)                              ____")
    print("____                                                                              ____")
    print("______________________________________________________________________________________")
def displayRods():
    print("______________________________________________________________________________________")
    print("____                             Rods                                             ____")
    print("____                                                                              ____")
    print("____  1. Jerkbait rod                  Price: (150.00)                            ____")
    print("____  2. Crainkbait rod                Price: (89.00)                             ____")
    print("____  2. A-rig rod                     Price: (250.00)                            ____")
    print("____  2. texas rig rod                 Price: (175.00)                            ____")
    print("____                                                                              ____")
    print("______________________________________________________________________________________")
def displayReels():
    print("______________________________________________________________________________________")
    print("____                             Reels                                            ____")
    print("____                                                                              ____")
    print("____  1. Shimano metanium              Price: (400.00)                            ____")
    print("____  2. Shimano sustain               Price: (600.00)                            ____")
    print("____  2. Abu garcia revo sc            Price: (150.00)                            ____")
    print("____  2. Diawa tatula                  Price: (175.00)                            ____")
    print("____                                                                              ____")
    print("______________________________________________________________________________________")
def displayClothing():
    print("______________________________________________________________________________________")
    print("____                             Clothing                                         ____")
    print("____                                                                              ____")
    print("____  1. Jacket                       Price: (75.00)                              ____")
    print("____  2. Pants                        Price: (50.00)                              ____")
    print("____  2. Shoes                        Price: (200.00)                             ____")
    print("____  2. Socks                        Price: (12.00)                              ____")
    print("____                                                                              ____")
    print("______________________________________________________________________________________")

def menuChoice():
    print("\n Which product line would you like to view? (1-4) \n")
    prodLineChoice = input("\n Choice: ")
    if(prodLineChoice == 1):
        displayTackle()
    elif(prodLineChoice == 2):
        displayRods()
    elif(prodLineChoice == 3):
        displayReels()
    elif(prodLineChoice == 4):
        displayClothing()
