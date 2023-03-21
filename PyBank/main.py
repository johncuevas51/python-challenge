import os

#module for reading CSV files
import csv

# Variables for output numbers
total_amount = 0
total_month = 0
maximum = ["", 0]
minimum = ["", 0]
begining_profit = 0
change_list = []

#enter path
csvpath = os.path.join('Resources','budget_data.csv')

#open CSV file
with open(csvpath) as csvfile:

#CSV reader specifies delimter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
 
#read the header row 
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


#reach each row of data after header
    for row in csvreader:
        total_amount= total_amount + int(row[1])
        total_month += 1


        # Look for Max and Min
        if total_month > 1:
            change = int(row[1]) - begining_profit
            change_list.append(change)
            begining_profit = int(row[1])
            if change > maximum[1]:
                maximum[1] = change
                maximum[0] = row[0]
            if change < minimum[1]:
                minimum[1] = change
                minimum[0] = row[0]

        else:
            begining_profit = int(row[1])


avg_change = round(sum(change_list)/(total_month - 1), 2)

output = f"""
Financial Analysis
----------------------------
Total Months: {total_month}
Total: ${total_amount}
Average Change: ${avg_change}
Greatest Increase in Profits: {maximum[0]} (${maximum[1]})
Greatest Decrease in Profits: {minimum[0]} (${minimum[1]})
"""

print(output)

with open("analysis/output_bank.txt", "w") as output_file:
    output_file.write(output)