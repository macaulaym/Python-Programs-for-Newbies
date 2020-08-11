import re

str = "Sat, hat, mat, pat"

#find words in which the first letter is btwn. the range h-m and end with "at" in the string provided.
allstr = re.findall("[h-m]at", str)

for i in allstr:
    print(i)
