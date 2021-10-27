#LAB - 13 - Using Functions to Implement a Caesar Cipher
import math

print("LAB 13 - Using Functions to Implement a Caesar Cipher")

#declaring the alphabet as a list of letters
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#print(len(alphabet))
#Length of alphabet is 26

#originalString = input("Please type the message to encrypt: ")
#print(originalString) - OK


#define function to get the input from the user - returns the input as a string
def getMessage():
    originalString = input("Please type the message to encrypt: ")
    return originalString

#define the shift amount to apply to the cypher
def getCypherKey():
    shiftAmount = input("Please enter a key (shift amount: 1-25): ")
    return shiftAmount

def listToString(aList):
    aString=""
    return(aString.join(aList))

#test variables
testMessage = "this is a test string with some words"
testShift = 3

print('---------')

originalIndexList=[]
for char in testMessage:
    if char in alphabet:
        originalIndexList.append((alphabet.index(char))+testShift)
    else:
        originalIndexList.append("-")

print('---------')

for i in range(0, len(originalIndexList)):
    if isinstance(originalIndexList[i], int):
        originalIndexList[i] += testShift
        if originalIndexList[i] >= len(alphabet)-1:
             originalIndexList[i] = originalIndexList[i] - 25

#encrypt stage
# convert alphabet indexes to readable letters
encryptedMessage = []

def encryptMessage():
    for i in range(0, len(originalIndexList)-1):
        if isinstance(originalIndexList[i], int):
            encryptedMessage.append(alphabet[originalIndexList[i]])
        else:
            encryptedMessage.append(" ")
    print(listToString(encryptedMessage))






print('---------')

print(originalIndexList)
