#LAB 14 - Creating File Handlers and Modules for Retrieving Information about Insulin

import json

print("LAB 14 - Creating File Handlers and Modules for Retrieving Information about Insulin")

def readJsonFile(myJsonFile):
    data = ""
    try:
        with open('insulin.json') as jsonFile:
            data = json.load(jsonFile)
    except IOError:
        print("Could not read file!")
    return data
