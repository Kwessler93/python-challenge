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
net_change = 0
Value_Total = 0
net_change = 0
GreatestIncrease = 0
GreatestIncrease_Date = 0
GreatestDecrease = 0
GreatestDecrease_Date = 0
average_net_change = 0

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)
   


    # Extract first row to avoid appending to net_change_list
    for row in reader:
        
        net_change_list = float(row[1])

    # Track the total and net change
        Value_Total += net_change_list
    
    if len(row) >2:
        previous_value = float(row[2])
        net_change += (net_change_list - previous_value)
    

    # Process each row of data
    for row in reader:

        # Track the total
        Value_Total_Months = len(row[0])

        Value_Total += net_change_list

        # Track the net change
        if len(row) >2:
            previous_value = float(row[2])
            net_change += (net_change_list - previous_value)


        # Calculate the greatest increase in profits (month and amount)
            date = row[0]

            if previous_value is not None:
                increase = net_change_list - previous_value
                if increase > GreatestIncrease:
                    GreatestIncrease = increase
                    GreatestIncrease_Date = date

            previous_value = net_change_list

        # Calculate the greatest decrease in losses (month and amount)
            if previous_value is not None:
                decrease = net_change_list - previous_value
                if decrease < GreatestDecrease:
                    GreatestDecrease = decrease
                    GreatestDecrease_Date = date

            previous_value = net_change_list

# Calculate the average net change across the months
    def average_net_change(net_change_list):
        if not net_change_list:
            return 0
        total_net = sum(net_change_list)
        count = len(row)
        average_net_change = total_net/count
        return average_net_change

# Generate the output summary
file_to_output = "budget_analysis.txt"

print("Financial Analysis")

print("------------------------")

print(f"Total Months: {total_months}")

print(f"Total: {Value_Total}")

print(f"Average Change: {average_net_change}")
      
print(f"Greatest Increase in Profits: {GreatestIncrease_Date} ({GreatestIncrease})")     

print(f"Greatest Decrease in Profits: {GreatestDecrease_Date} ({GreatestDecrease})")

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(budget_analysis.txt)
