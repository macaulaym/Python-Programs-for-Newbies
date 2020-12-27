import re

#\w [a-z|A-Z|0-9|_]
#\W [^a-z|A-Z|0-9]

telephonenos = "412-555-121"

if re.search("\w{3}-\w{3}-\w{4}", telephonenos):
    print("Telephone number provided is valid")
else:
    print("Telephone number provided is not valid!")