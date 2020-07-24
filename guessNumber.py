#import random module
import random

#generate random number
x=random.randint(1,100)

#say I am thinking of a number
print ('I am thinking of a number between 1 and 100')

#ask the user to guess your number
guess=input('Please guess my number: ')

#while guess is not equal to x
while guess!=(x):
    if guess>x: #if guess is bigger than x
        guess=input('That number is too high, please guess again: ')
        
    elif guess<x: #if guess is lower than x
        guess=input('That number is too low, please guess again: ')

print( 'You have guessed correctly, well done!') #well done message
