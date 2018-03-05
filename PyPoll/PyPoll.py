import os
import csv
import collections

voterid =[]
country=[]
candidateOr= []
candidateSet = []
temp = 0

filepath = os.path.join("Resources", input("Please Enter the Filename: "))

with open(filepath, newline= '') as csvfile:
    
    filereader = csv.reader(csvfile, delimiter = ",")
    next(filereader, None)
    for row in filereader:
        voterid.append(row[0])
        country.append(row[1])
        candidateOr.append(row[2])
        count = len(voterid)
        candidateSet = set(candidateOr)
        countrep = collections.Counter(candidateOr)

print("Total Votes : " + str(count))
print("Total Candidates Participated: " + str(candidateSet))  
for k,val in countrep.items():
    perctgvotes = round((val/count)*100,2)
    print(k + "  "  + str(perctgvotes) + "%" + " (" + str(val) + ")")
    if val >= temp:
        temp = val
    
for k,val in countrep.items():
    if temp == val:
        print("Winner is : " + k + " with votes of " + str(val))