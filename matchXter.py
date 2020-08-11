import re

randomstr = "12345"

#prints out the returned number of digit 5 matches found in randomstr
print(len(re.findall("\d{5}", randomstr)), " number of matches found.")