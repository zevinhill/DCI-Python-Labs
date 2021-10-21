import math

print("LAB-7: Working with Conditionals")

# userReply = input("Do you need help finding a package? (Enter Yes or No)")

# if userReply == "Yes":
#     print(userReply)
# else:
#     print("no go!")


userReply = input("Choose an option: Buy stamps?(type stamp); Make a copy?(type copy); Buy an envelope?(type envelope)")

if userReply == "stamp":
    print("Sorry! No stamps today, please come back some other day.")
elif userReply == "copy":
    numberOfCopies = input("How many copies do wish? (type a number)")
    print(f'They will be ready in {int(numberOfCopies) * 0.2} minutes.')
elif userReply == "envelope":
    print("Sorry! There was an accident with the envelopes in the wharehouse, please come back some other day.")
else:
    print("We don't have that in stock as well...Please come back some other day.")