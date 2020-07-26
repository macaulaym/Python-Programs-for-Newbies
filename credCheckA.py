print("Create a username") #tell the user to create a username
username = input() # input the username
names= [] #add a list
names.append(username) #put the username in the list

print("Create a password") #tell the user to create a password.
password = input() #input the password
passwords = [] #add a list
passwords.append(password) #add the password to the list

print("Enter your username") #prompt the user to enter their username
user1 = input() #username input

if user1 in names: #check if the input is in the list
    print("enter password")#if the input is there, enter password
    pass1 = input() #check if the password is in the list
    if pass1 in passwords: #if it is stored
        print("Welcome") #correct user and password
    else:
        print("Incorrect password")
else:
    print("Invalid username")

    
