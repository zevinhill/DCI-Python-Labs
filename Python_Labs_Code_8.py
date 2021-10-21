#LAB-8 Working with Loops
import random

print("LAB 8 - Working with Loops")

print("Welcom to the 'DCI Guess tha Numbah' game")
print("Rules are simple: you need to guess the number I'm thinking.")

secretNumber = random.randint(1,100)
print(secretNumber)

user_guess = int(input("Pick a number between 1 and 100: "))
while user_guess != secretNumber:
    print("please try again!")
    user_guess = input("Pick a number between 1 and 100: ")
else:
    print(f'Nice!! you got it right..the number is {user_guess} ! Try playing the lottery.')

