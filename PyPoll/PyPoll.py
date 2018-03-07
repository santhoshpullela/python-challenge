import os
import csv
import collections

voterid =[]
country=[]
candidateOr= []
candidateSet = []
temp = 0
f = open("PyPoll_Output.txt", 'w')
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
print("Election Results" + "\n" + "-------------------------" + "\n" + "Total Votes: " + str(count) + "\n" + "-------------------------" + "\n")
f.write("Election Results" + "\n" + "-------------------------" + "\n" + "Total Votes: " + str(count) + "\n" + "-------------------------" + "\n")
for k,val in countrep.items():
    perctgvotes = round((val/count)*100,2)
    print(k + "  "  + str(perctgvotes) + "%" + " (" + str(val) + ")")
    f.write(k + "  "  + str(perctgvotes) + "%" + " (" + str(val) + ")" + "\n")
    if val >= temp:
        temp = val
    
for k,val in countrep.items():
    if temp == val:
        print("Winner is : " + k )
        winner = k
        wincount = val

f.write("Winner is :" + winner )
f.close()    