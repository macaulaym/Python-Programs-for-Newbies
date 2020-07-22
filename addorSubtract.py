operation = input("Please indicate whether you woukd like to add or subtract? ")

num1 = int(input("Please provide an integer ---> "))

num2 = float(input("Please provide a float ---> "))



if operation == "-" or operation == "substraction":

print(num1 - num2)

elif operation == "+" or operation == "adition":

print(num1 + num2)

else:

print("I don't understand operation")
