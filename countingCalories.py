gender = input("Are you a man or a woman? ---> ")

cal = int(input("How many calories did you eat? --> "))

if gender == "man" or gender == "Man":

    print("You have" , 2500 - cal , "calories left")

elif gender == "woman" or gender == "Woman":

    print("You have" , 2000 - cal , "calorie left")

else:

    print("I don't know your gender")
