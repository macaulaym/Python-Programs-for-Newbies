import random   
compnum=random.randint(1,100)
user=int(input("Please guess my number:\n"))
while user!=compnum:
    if user>compnum:
        user=int(input("That number is too high, please try again:\n"))
    else:
        user=int(input("That number is too low, please guess again:\n"))
print("You have guessed correctly, well done!")


