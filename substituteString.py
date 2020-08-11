import re

mystr = "hat, mat cat, sat, pat"

#compile the string that starts with character 'r' and ends with "at" using the pattern object method substitute
regex = re.compile("[c]at")

#substitute the word 'chat' in the string mystr
mystr = regex.sub("chat", mystr)

print(mystr)