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
print("\nElection Results")
print("\n-------------------------")
print(f"\nTotal Votes: {total_votes}")
print("\n-------------------------")

# Calculate and print the percentage of votes for each candidate
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    print(f"\n{candidate}: {percentage:.3f}% ({votes})")

print("\n-------------------------")

# Find the winner
winner = max(candidates, key=candidates.get)

# Print winner
print(f"\nWinner: {winner}")
print("\n-------------------------")

###################################################################################################################
####################################### PRINT TXT #################################################################

# save the output file path    
output_file = os.path.join("Analysis", "Election_Results.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as file:
    file.write("\nElection Results\n")
    file.write("\n--------------------------------\n")
    file.write(f"\nTotal Votes: {total_votes}\n")
    file.write("\n--------------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"\n{candidate}: {percentage:.3f}% ({votes})\n")  
    file.write("\n--------------------------------\n")
    file.write(f"\nWinner: {winner}\n")
    file.write("\n--------------------------------\n")
