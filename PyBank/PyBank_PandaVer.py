import os
import pandas as pd
filepath = os.path.join("Resources" , input("Please enter the file name: "))
#Read CSV File
bank_df = pd.read_csv(filepath)
#Get Total Months Count and Total Revenue
months_count , total_revenue = bank_df["Date"].count() , bank_df["Revenue"].sum()
#Create a new column with revenue change with each month and do necessary calculations
bank_df["change_revenue"] = bank_df["Revenue"].shift(-1) - bank_df["Revenue"]
average_changerev = bank_df["change_revenue"].mean()
bank_df.change_revenue = bank_df.change_revenue.shift(+1)
grt_incr_rev , grt_decr_rev = bank_df["change_revenue"].max() , bank_df["change_revenue"].min()
grt_incr_date, grt_decr_date = bank_df.loc[bank_df['change_revenue'] == grt_incr_rev,'Date'].values[0] , bank_df.loc[bank_df['change_revenue'] == grt_decr_rev,'Date'].values[0]
#Write Output
print("Total Number of months: " + str(months_count) + "\n" + "Total Revenue         : $" + str(total_revenue) + "\n"  + "Average Revenue       : $" + str(average_changerev) )
print("Greatest Increase in Revenue is on " + str(grt_incr_date) + " and the value is $"  + str(grt_incr_rev))
print("Greatest Decrease in Revenue is on " + str(grt_decr_date) + " and the value is $"  + str(grt_decr_rev))
f = open("PyBankOutput.txt", 'w')
f.write("*******Financial Analysis*******\n")
f.write("_________________________________\n")
f.write("Total Number of months: " + str(months_count) + "\n" + "Total Revenue         : $" + str(total_revenue) + "\n" + "Average Revenue       : $" + str(average_changerev) + "\n" )
f.write("Greatest Increase in Revenue is on " + str(grt_incr_date) + " and the value is $" + str(grt_incr_rev) + "\n")
f.write("Greatest Decrease in Revenue is on " + str(grt_decr_date) + " and the value is $" + str(grt_decr_rev) + "\n")
f.close()    