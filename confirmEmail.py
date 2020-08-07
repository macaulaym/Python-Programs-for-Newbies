import re
email = input("enter your email address")
m = re.search("(@)", email)
if m:
    print("your email is valid")
else:
    print ("invalid email address")
