import os
import csv

# Module for reading CSV files
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #  Header row
    header = next(csvreader)

    # Loop through the rows in the CSV file
    for row in csvreader:
        # Count total votes
        total_votes += 1

        # Count votes for each candidate
        candidate = row[2]
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Write the results to a text file
output_path = os.path.join("Analysis","election_results.txt")
with open(output_path, "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("-------------------------\n")
    output_file.write(f"Total Votes: {total_votes}\n")
    output_file.write("-------------------------\n")

    # Calculate  the percentage of votes each candidate won
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
        output_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")

        # Find the winner
        if votes > winner_votes:
            winner = candidate
            winner_votes = votes

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    output_file.write("-------------------------\n")
    output_file.write(f"Winner: {winner}\n")
    output_file.write("-------------------------\n")
