import re

str = "Sat, hat, mat, pat"

#find words that start with s/h/m/p and end with "at" in the string provided.
allstr = re.findall("[h-m]at", str)

for i in allstr:
    print(i)