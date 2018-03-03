import os
import csv


budgetrev =[]
months=[]
filepath = os.path.join("Resources", "budget_data_1.csv")
#oppath = os.path.join('output', 'PyBankOutput.txt')

with open(filepath, newline ='') as csvfile:
    filereader = csv.reader(csvfile, delimiter = ",")
    next(filereader, None)
    for row in filereader:
        months.append(row[0])
        budgetrev.append(int(row[1]))  
        count = len(budgetrev)
        totalrev = sum(budgetrev)
        avgrev = round((totalrev/count),2)
        max_value = max(budgetrev)
        min_value = min(budgetrev)

budgetAnalysis = dict(zip(budgetrev,months))
for k,v in budgetAnalysis.items():
    if k == max_value:
        maxdate = v
    if k == min_value:
        mindate = v

print("Total Number of months: " + str(count))
print("Total Revenue         : $" + str(totalrev)) 
print("Average Revenue       : $" + str(avgrev))
print("Greatest Increase in Revenue is on " + str(maxdate) + " and the value is "  + str(max_value) )
print("Greatest Decrease in Revenue is on " + str(mindate) + " and the value is "  + str(min_value) )

f = open("PyBankOutput.txt", 'w')
f.write("*******Financial Analysis*******\n")
f.write("_________________________________\n")
f.write("Total Number of months: " + str(count) + "\n")
f.write("Total Revenue         : $" + str(totalrev) + "\n")
f.write("Average Revenue       : $" + str(avgrev) + "\n")
f.write("Greatest Increase in Revenue is on " + str(maxdate) + " and the value is " + str(max_value) + "\n")
f.write("Greatest Decrease in Revenue is on " + str(mindate) + " and the value is " + str(min_value) + "\n")
f.close()    