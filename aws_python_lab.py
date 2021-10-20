#LAB-2
#Ex.25 editing a python file
print("LAB 2 - Numeric Data Types")

print("Python has three numeric types: int, float, and complex")


#Ex.31 Creating a variable

myvalue = 1
print(myvalue)
print(type(myvalue)) #returns variable type
print(str(myvalue) + ' is of data type ' + str(type(myvalue)) ) #transform variable to string and concatenates strings

print("------")

#Ex.45
myvalue = False
print(myvalue)
print(type(myvalue)) #returns variable type
print(str(myvalue) + ' is of data type ' + str(type(myvalue)) ) #transform variable to string and concatenates strings

print("------")

#LAB-3
#String Data Type

print("LAB 3 - String Data Type")

#Exercise 1: Introducing the string data type
#Ex.12
myString="this is a string"
print(myString)
print(type(myString))
print(str(myString) + ' is of data type ' + str(type(myString)) ) #transform variable to string and concatenates strings

print("------")

#Ex.22
firstsring = "1st string"
secondstring = "2nd string"
thirdstring = firstsring + secondstring
print(thirdstring)

print("------")


#Ex.26 - reading user imnput from terminal/StdIn

# name = input("What is your name : ")
# color = input("What is your favorite color : ")
# animal = input("What is your favorite animal: ")
# print(name+color+animal)
# print("{} + {} + {} ".format(name,color,animal)) #ATT: the .format function is directed in order to the containers in the {}

#LAB-4
#Working with Lists, Tuples, and Dictionaries
# [] - list
# {} - dictionary
# () - Tuple - ATT: NOT ORDERED, NOT CHANGEABLE

print("------")

print("LAB 4 - Lists, Tuples, and Dictionaries")

myfruitlist = ["banana","apple","cherry","pinapple"] #LIST
print(myfruitlist)
print(type(myfruitlist))
print(type(myfruitlist[2]))
print(myfruitlist[2])

myfruitlist[1] = "pear"
print(myfruitlist) #ATT: changed fruit in position 2 - [1]

print("------")

myFinalAnswerTuple = ("apple","cherry","pinapple") #TUPLE
print(myFinalAnswerTuple[0])
print(type(myFinalAnswerTuple))
print(type(myFinalAnswerTuple[0]))
print(myFinalAnswerTuple[0])

print("------")
#myFinalAnswerTuple[0] = "mandarine"
#TypeError: 'tuple' object does not support item assignment

myFavoriteFruitDictionary = {"Breakfast":"Pinapple","Lunch":"Orange","Diner":"watermelon"}

mySecondFavoriteFruitDictionary = {
    "Breakfast":"Pear",
    "Lunch":"Grape",
    "Diner":"Banana"
}

print("------")
print(myFavoriteFruitDictionary)
print("------")
print(mySecondFavoriteFruitDictionary)
print("------")
print(myFavoriteFruitDictionary["Lunch"])
print("------")

for fruit in myFavoriteFruitDictionary:
    print(fruit)

print("------")    

for fruit in myFavoriteFruitDictionary:
    print(myFavoriteFruitDictionary[fruit])

print("------")

for meal in mySecondFavoriteFruitDictionary:
    print(meal)
    
print("------")

#LAB-5
#Categorizing Values

print("LAB 5 - Categorizing Values")

myMixedTypeList = [34, "apple", 5.76, False, "Granola"]

for item in myMixedTypeList:
    print(item)
    print(type(item))

for item in myMixedTypeList:
    print()
    print("The {}th element of the list is {}, and is of type {}".format(myMixedTypeList.index(item)+1,item,type(item))) 
    
    #ATT: Close attention to the way you call the "index" method of the List class and the "type" function with "item" as an argument   
print("------")
