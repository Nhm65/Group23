

def userCreat():
    
    import userLogin

    print("\nPlease enter a new username and password: ")
    username = input("\n Enter a new Username: ")
    password = input("\n Enter a new Password: ")

    # call the Mysql database and make that connection
    import mysql.connector
    import sys

    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "Users" #names in xamp
        )
        print("\n Connection was successful \n")
    except:
        print("\nConnection failed\n")
        sys.exit()

        #cursor to send queries through
        cursor = connection.cursor()

            #query insert the username and password into the database
        query = "INSERT INTO Users (Username, Password) VALUES (%s,%s)"
        data = (username,password)

            #sends query with the data
        cursor.execute(query, data)

            #commit the changes
        connection.commit

            #show the changes made to the database
        print(cursor.rowcount, "Username and password inserted")
        print()

            #close the cursor
        cursor.close()
        connection.close()
