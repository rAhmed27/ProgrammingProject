def register():
    loginDB = open("database.txt", "r")
    username = input("Enter username: ")
    password = input("Enter password: ")
    passwordC = input ("Confirm password: ")
    if password != passwordC:
        print("Password unconfirmed. Please try again!")
        register()
    if len(password) <= 8:
        print("Password too short. Please try again!")
        register()    

    
register()
