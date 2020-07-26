accountsUsername=[]
accountsPassword=[]
def accountCreate(username,password):
    print('Thank you for creating your account, it has been saved to the system')
    accountsUsername.append(username)
    accountsPassword.append(password)
print('Type accountCreate and then in brackets put your username followed by a comma then followed by your password')
def login(username1,password1):
    accountVerified=int(0)
    for index in range (len(accountsUsername)):
        if accountsUsername[index]==username1 and accountsPassword[index]==password1:
            print('Welcome', username1 )
            accountVerified=1
    if accountVerified!=1:
        print('Invalid Credentials')
            
