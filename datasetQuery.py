#This program outputs a dictionary data set containing only the names and ages from the string data set.

#import the re module
import re

#Create a variable containing a data set string
NameAge = '''Jill is 22 and Tom is 33, Gabriel is 44 and Ruth is 21'''

ages = re.findall(r'\d{1,3}', NameAge)
names = re.findall(r'[A-Z][a-z]*', NameAge)

ageDict = {}
x = 0

#for loop
for eachname in names:
    ageDict[eachname] = ages[x]

    x+=1
    print(ageDict)

