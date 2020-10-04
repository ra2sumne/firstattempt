#Import library
import pandas as pd
import numpy as np
from pathlib import Path

#joining path
csvpath = Path("/Users/rawlricsumner/Desktop/FinTech_Boot_Camp/python-homework/Resources/budget_data.csv")
budget_data = pd.read_csv(csvpath)

# open and read csv
budget_data.head()
budget_data.set_index(pd.to_datetime(budget_data['Date'], infer_datetime_format=True), inplace=True)
budget_data.drop(columns="Date", inplace=True)
largest_increase = budget_data.nlargest(1, 'Profit/Losses')
largest_increase
largest_decrease = budget_data.nsmallest(1, 'Profit/Losses')
largest_decrease
total = budget_data.iloc[2].sum()
print(total)

total_months = len(budget_data)
total_months

print("Financial Analysis")

print("_________________________________________________________________")
print("Total Months:" +str(total_months))
print("Total: $" +str(total))
print("Average Change:" +str())
print("Greatest Increase in Profits:" +str(largest_increase))
print("Greatest Decrease in Profits:" +str(largest_decrease))

# output

file = open("output.txt","w")
file.write("Financial Analysis")

file.write("____________________________________________________________" + "\n")

file.write("Total Months: " + str(total_months) + "\n")

file.write("Total: $" +str(total) + "\n")

file.write("Average Change: " + "\n")

file.write("Greatest Increase in Profits: " +str(largest_increase) + "\n")

file.write("Greatest Decrease in Profits: " +str(largest_decrease) + "\n")

file.close
