import re

str = "ever tried, ever failed, no matter, try again, fail again, fail better."

#Use the finditer method to iterate through to find the start and end index of the word "ever"
for i in re.finditer("ever", str):

    #convert into a tuple
    tupResult = i.span()

    print(tupResult)