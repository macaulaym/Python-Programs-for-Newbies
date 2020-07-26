def login():
    reg=input("Are you registered? Y/N ")
    database=[["Gleed", "pass1"],["Smith","pass2"],["Kosmo","pass3"]]
    if reg=="Y" or reg =="y":
        usnm=input("Username: ")
        pswd=input("Password: ")
        for x in range(len(database)):
            if database[x][0]==usnm:
                if database[x][1]==pswd:
                    return "Yay! You are logged in!"
                else:
                    return "Sorry your password was incorrect."
            else:
                return "Sorry your username was incorrect"
        print("You have logged in successfully.")
    else:
        usnm=input("Please enter a username: ")
        check=False
        while check == False:
            for x in range(len(database)):
                if database[x][0]==usnm:
                    check=False
                    usnm=input("That username has been taken. Please enter a different username: ")
                else:
                    check=True
        
        pswd1=input("Please enter your password: ")
        pswd2=input("Please enter your password again: ")
        while pswd1!=pswd2:
            print("Your passwords don't match.")
            pswd1=input("Please enter your password: ")
            pswd2=input("Please enter your password again: ")
        database+=[usnm,pswd1]
        print("You are now registered, please login.\n")
        login()



