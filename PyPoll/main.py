# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Specify the path to your CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

# Initialize variables to store the data
total_votes = 0
candidates = {}
winner = ""

# Open and Read the CSV file
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row if it exists
    header = next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        #voter_id, county, candidate = row
        total_votes += 1
        candidate = row[2]
        
        # Update candidate vote count
        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

print("-------------------------")

# Find the winner
winner = max(candidates, key=candidates.get)

# Print winner
print(f"Winner: {winner}")
print("-------------------------")