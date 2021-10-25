#LAB 12 - Calculating the Net Charge of Insulin by Using Python Lists and Loops

print("LAB 12 - Calculating the Net Charge of Insulin by Using Python Lists and Loops")

# Store the human preproinsulin sequence in a variable called preproinsulin:  
preproInsulin = "malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"  
# Store the remaining sequence elements of human insulin in variables:  
lsInsulin = "malwmrllpllallalwgpdpaaa"  
bInsulin = "fvnqhlcgshlvealylvcgergffytpkt"  
aInsulin = "giveqcctsicslyqlenycn"  
cInsulin = "rreaedlqvgqvelgggpgagslqplalegslqkr"  
insulin = bInsulin + aInsulin
print(insulin)
print(len(insulin))
#count of aa in insulin

# Example: print(float(insulin.upper().count("Y")))


#Creation of a dictionary whose keys are values from a list, and whose values are the count() results for each of those keys (aa)
seqCount = ({x:float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

#Creation of a dictionary
#Note: Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation.
pKR = {
    'y': 10.07, 
    'c': 8.18,
    'k': 10.53,
    'h': 6.00,
    'r': 12.48,
    'd': 3.65,
    'e': 4.25
    }

pH = 0
while pH <= 14:
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH +=1