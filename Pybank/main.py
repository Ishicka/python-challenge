import os
import csv

# Module for reading CSV files
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
prior_profit_loss = 0
profit_loss_change = 0
changes = []
months = []


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

 # Loop through the rows in the CSV file
    for row in csvreader:
        # Count total months
        total_months += 1

        # Calculate net total
        net_total += int(row[1])

        # Calculate change in profit/loss
        if total_months > 1:
            profit_loss_change = int(row[1]) - prior_profit_loss
            changes.append(profit_loss_change)
            months.append(row[0])

        # Set the current profit/loss as the previous for the next iteration
        prior_profit_loss = int(row[1])

# Calculate average change
average_change = round(sum(changes) / len(changes), 2)

# Find the greatest increase and decrease in profits
greatest_increase = max(changes)
greatest_increase_month = months[changes.index(greatest_increase)]
greatest_decrease = min(changes)
greatest_decrease_month = months[changes.index(greatest_decrease)]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")


# Results to a text file
output_path = os.path.join("Analysis","Analysis.txt")
with open(output_path, "w") as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")



