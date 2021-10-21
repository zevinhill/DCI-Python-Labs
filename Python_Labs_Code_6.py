#LAB-6 - Working with Composite Data Types
print("LAB-6: Working with Composite Data Types")

#import modules to work with csv files and file management (copy)
import csv
import copy
import os

#definition of a dictionary - define the Key structure of the dictionary
myVehicle = {
    "vin" : "",
    "make" : "",
    "model" : "",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0,
}

#
for key, value in myVehicle.items(): #we use the .items() to define each key:Value pairs of the dictionary
    #print("{} : {}".format(key,value))
    print(f'{key} {value}')

#ATT: at this point no use was made of the csv file yet

myInventoryList = [] # List that will hold the car inventory results
#ATTENTION: each value from this list will be a dictionary holding the key-pair values for each car

workingDirectory = os.getcwd() #attention: workaround to avoid to explicitely declare the full path of the csv file upon invoking the "open" method
print(workingDirectory)

with open(f'{workingDirectory}/DCI-Python-Labs/car_fleet.csv') as csvFile: # the "with" function from the "copy" module allows to access the csv file
    csvReader = csv.reader(csvFile, delimiter=',') # the .reader is a method from the csv module
    linecount = 0 # initial counter
    for row in csvReader:
        if linecount == 0:
            print(f'colums names are: {", ".join(row)}')
            linecount += 1
        else:
            print(f'vin: {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
            currentVehicle = copy.deepcopy(myVehicle) # puts the contents of the file into memory to be processed
            currentVehicle["vin"] = row[0]
            currentVehicle["make"] = row[1]
            currentVehicle["model"] = row[2]
            currentVehicle["year"] = row[3]
            currentVehicle["range"] = row[4]
            currentVehicle["topSpeed"] = row[5]
            currentVehicle["zeroSixty"] = row[6]
            currentVehicle["mileage"] = row[7]
            myInventoryList.append(currentVehicle)
            linecount += 1
    print(f'Processed {linecount} lines')
    
    for myCarProperties in myInventoryList:
        for key, value in myCarProperties.items():
            print("{} : {}".format(key,value))
            print("--------")
    
    print(type(myInventoryList[1])) #confirmation that each "value" from the myInventory List is in fact a dictionary
    print(myCarProperties['vin']) #will only show the value for the last item in myVehicle, given it was the last iteration of the for loop
