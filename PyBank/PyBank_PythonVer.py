import os
import csv
#Declarations - Varibales, Lists
budgetrev =[]
changerev = []
months=[]
tempchg = 0
filepath = os.path.join("Resources",input("Please Enter the Filename: "))
#oppath = os.path.join('output', 'PyBankOutput.txt')
# Opening the CSV File and creating the required lists
with open(filepath, newline ='') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ",")
    next(filereader, None)
    for row in filereader:
        months.append(row[0])
        budgetrev.append(int(row[1]))         
# Calculations
count = len(budgetrev)
totalrev = sum(budgetrev)      
for index,item in enumerate(budgetrev):
    tempchg = item - tempchg
    changerev.append(tempchg)
    tempchg = item
budgetAnalysis = dict(zip(changerev,months))
changerev.pop(0)
avgrev = round(sum(changerev)/(count-1),2)
max_value = max(changerev)
min_value = min(changerev)

for k,v in budgetAnalysis.items():
    if k == max_value:
        print(k,v)
        maxdate = v
    if k == min_value:
        print(k,v)
        mindate = v
# Write Output total Terminal
print("Total Number of months: " + str(count))
print("Total Revenue         : $" + str(totalrev)) 
print("Average Revenue       : $" + str(avgrev))
print("Greatest Increase in Revenue is on " + str(maxdate) + " and the value is $"  + str(max_value) )
print("Greatest Decrease in Revenue is on " + str(mindate) + " and the value is $"  + str(min_value) )
# Write Output to a text file
f = open("PyBankOutput.txt", 'w')
f.write("*******Financial Analysis*******\n")
f.write("_________________________________\n")
f.write("Total Number of months: " + str(count) + "\n")
f.write("Total Revenue         : $" + str(totalrev) + "\n")
f.write("Average Revenue       : $" + str(avgrev) + "\n")
f.write("Greatest Increase in Revenue is on " + str(maxdate) + " and the value is $" + str(max_value) + "\n")
f.write("Greatest Decrease in Revenue is on " + str(mindate) + " and the value is $" + str(min_value) + "\n")
f.close()    