# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import os
import csv

# Files to load and output (update with correct file paths)
file_to_load = '/Users/kimberlywessler/python-challenge/PyBank/Resources/budget_data.csv'  # Input file path
file_to_output = '/Users/kimberlywessler/python-challenge/PyBank/Analysis/budget_analysis.txt'  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
previous_value = None
GreatestIncrease = 0
GreatestDecrease = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        total_months += 1
        current_value = int(row[1])
        total_net += current_value

        if previous_value is not None:
            net_change = current_value - previous_value
            net_change_list.append(net_change)

        # Calculate the greatest increase in profits (month and amount)
        
            if net_change > GreatestIncrease:
                GreatestIncrease = net_change
                GreatestIncrease_Date = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        
            if net_change < GreatestDecrease:
                GreatestDecrease = net_change
                GreatestDecrease_Date = row[0]

        previous_value = current_value

# Calculate the average net change across the months

if net_change_list:
    average_net_change = sum(net_change_list)/len(net_change_list)
else:
    average_net_change = 0
    

# Generate the output summary

print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: {total_net}")
print(f"Average Change: {average_net_change:.2f}")
print(f"Greatest Increase in Profits: {GreatestIncrease_Date} ({GreatestIncrease})")     
print(f"Greatest Decrease in Profits: {GreatestDecrease_Date} ({GreatestDecrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    writer = csv.writer(txt_file)

    txt_file.write("Financial Analysis\n")
    txt_file.write("------------------------\n")
    txt_file.write(f"Total Months: {total_months}\n")
    txt_file.write(f"Total: ${total_net}\n")
    txt_file.write(f"Average Change: ${average_net_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profits: {GreatestIncrease_Date} (${GreatestIncrease})\n")     
    txt_file.write(f"Greatest Decrease in Profits: {GreatestDecrease_Date} (${GreatestDecrease})\n")