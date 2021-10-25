#LAB-8 Working with Loops
import random

print("LAB 8 - Working with Loops")

print("Welcom to the 'DCI Guess tha Numbah' game")
print("Rules are simple: you need to guess the number I'm thinking.")

secretNumber = random.randint(1,100)
print(f'secretNumber is {secretNumber}')

user_guess = int(input("Pick a number between 1 and 100: "))
#user_guess = input("Pick a number between 1 and 100: ")
print(type(user_guess))
print(user_guess)


while user_guess != secretNumber:
    print("please try again!")
    user_guess = int(input("Pick a number between 1 and 100: "))
    print(type(user_guess))
    print(user_guess)
else:
    print(f'Nice!! you got it right..the number is {user_guess} ! Try playing the lottery.')

