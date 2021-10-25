#LAB-10 Preparing to Analyze Insulin with Python

# Bonus: Cleaning preproinsulin-seq.txt programmatically
# # Cleaning source data files is a common task in 
# computer programming. You could programmatically clean preproinsulin-seq.txt 
# in several ways—for example, by using Bash, Python, or another programming 
# language of choice. 
# Try using regex to 
# programmatically strip the file of ORIGIN, 
# its numbers, 
# the two slashes (//), 
# spaces, and 
# line breaks or return carriages. 
# You could also confirm programmatically 
# that the file has 110 characters.
import re

print("LAB 10 - #LAB-10 Preparing to Analyze Insulin with Python")



#opening the file
with open('preproinsulin-seq.txt') as rawFile: # opens file and returns its content as a variable (rawFile) in this case 
    #'print(rawFile.readline()) #the .readline outputs the 1st line
    stringedFile = str(rawFile.read()) #rawFile is not a string originally - hence needs to be converted
    #print(type(stringedFile))
    #print(stringedFile)
    myMatchingStrings = re.findall(r"[a-z]\w+", stringedFile, re.MULTILINE)
    #print(len(myMatchingStrings))

with open('cleanPreproinsulin-seq.txt','w') as cleanSeqFile: #creates new file  - ATT: 'w' option in the 'open' method allows to write into it
    cleanSeqFile.write(myMatchingStrings) #like this, it will always overwrite what is in there

fullProteinSeq = "" #initializes a string that will hold the full sequence of aminoacids
for proteinBlock in myMatchingStrings:
    fullProteinSeq += proteinBlock #concatenate the various sequence blocks into one string
print(fullProteinSeq)






# REGEX (in Python format) EXPRESSION FOR THE PROTEIN SEQUENCES "[a-z]"gm
# myMatchingStrings = re.findall(r"[a-z]", someLines)
# print(someLines)




# with open('preproinsulin-seq.txt') as rawFile: # opens file and returns its content as a variable (rawFile) in this case 
#     #'print(rawFile.readline()) #the .readline outputs the 1st line
#     someLines = rawFile.readlines()
#     print(len(someLines))
#     print(type(someLines))
#     for item in someLines:
#         print(item)
        


# with open('cleanPreproinsulin-seq.txt','a') as cleanFile: #creates new file  - ATT: 'a' option in the 'open' method allows to write-APPEND into it without overwriting it   
#     cleanFile.write('appendable text')    

