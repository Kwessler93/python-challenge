# -*- coding: UTF-8 -*-
"""PyPoll Homework Starter File."""

# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = '/Users/kimberlywessler/python-challenge/PyPoll/Resources/election_data.csv'  # Input file path
file_to_output = '/Users/kimberlywessler/python-challenge/PyPoll/Analysis/election_analysis.txt'  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast
percentage = 0
winning_count = 0
winning_candidate = ""

# Define lists and dictionaries to track candidate names and vote counts
candidate_votes = {}
vote_list = []

# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in vote_list:
            vote_list.append(candidate_name)
            candidate_votes[candidate_name] = 0

        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

         # Print the total vote count (to terminal)
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("--------------------------")

    # Open a text file to save the output
with open(file_to_output, "w") as txt_file: 

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("--------------------------\n")

        # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in vote_list:
        votes = candidate_votes[candidate_name]
        percentage = (votes/total_votes) * 100

        # Print and save each candidate's vote count and percentage
        print(f"{candidate_name}: {percentage:.2f}% ({votes})")
        txt_file.write(f"{candidate_name}: {percentage:.2f}% ({votes})\n") 

     # Update the winning candidate if this one has more votes
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name

    # Generate and print the winning candidate summary
    print("--------------------------")
    print(f"Winner: {winning_candidate}")
    print("--------------------------")
    
    txt_file.write("--------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write("--------------------------\n")