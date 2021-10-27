#LAB 14 - Creating File Handlers and Modules for Retrieving Information about Insulin
import jsonFileHandler

print("LAB 14 - Creating File Handlers and Modules for Retrieving Information about Insulin")

data = jsonFileHandler.readJsonFile('insulin.json')

if data != "":
    bInsulin = data['molecules']['bInsulin']
    aInsulin = data['molecules']['aInsulin']
    insulin = bInsulin + aInsulin #new variable - not defined in the json file
    molecularWeightInsulinActual = data['molecularWeightInsulinActual']
    print('bInsulin: ' + bInsulin)
    print('aInsulin: ' + aInsulin)
    print('molecularWeightInsulinActual: ' + str(molecularWeightInsulinActual))
else:
    print("Error. Exiting program")

aaList = list(data['weights'].keys())
# print(type(aalist))
# print(aalist)

aaWeights = data['weights']
aaCountInsulin = ({x: float(insulin.upper().count(x)) for x in aaList}) # dictionary with keys from aaList(x) and values as the result of the count of occurrences in the sequence block 
molecularWeightInsulin = sum({x: (aaCountInsulin[x]*aaWeights[x]) for x in aaList}.values())
print("The rough molecular weight of insulin: " + str(molecularWeightInsulin))
print("Percent error: " + str(((molecularWeightInsulin - molecularWeightInsulinActual)/molecularWeightInsulinActual)*100))