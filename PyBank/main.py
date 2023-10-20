# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Specify the path to your CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

# Initialize variables to store the data
total_profit_losses = 0
total_changes = 0
previous_profit_losses = None
total_number_of_months = 0
greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

# Open and read the CSV file
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Skip the header row if it exists
    next(csvreader)

    # Loop through each line in the file
    for row in csvreader:
        date, profit_losses = row
        profit_losses = int(profit_losses)
    
        # Calculate changes in profit/loss and total number months
        if previous_profit_losses is not None:
            change = profit_losses - previous_profit_losses

            # Update the greatest increase and decrease
            if change > greatest_increase_amount:
                greatest_increase_date = date
                greatest_increase_amount = change
            elif change < greatest_decrease_amount:
                greatest_decrease_date = date
                greatest_decrease_amount = change

            total_changes += change
            total_number_of_months += 1

        # Update previous profit/loss for the next iteration
        previous_profit_losses = profit_losses

        # Update the total profit/loss
        total_profit_losses += profit_losses

# Calculate the average change
average_change = round(total_changes / total_number_of_months,2)

# Print the results
print(f'Financial Analysis')
print(f'-----------------------------------------')
print(f'Total Months: {total_number_of_months+1}')   # because we skip a row when previous_profit_losses = None
print(f'Total: ${total_profit_losses}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})') 

###################################################################################################################
####################################### PRINT TXT #################################################################

# save the output file path    
output_file = os.path.join("Analysis", "output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(['Financial Analysis'])
    writer.writerow(['------------------------------------'])
    writer.writerow(['Total Months:'])
    writer.writerow(['Total:'])
    writer.writerow(['Average Change:'])
    writer.writerow(['Greatest Increase in Profits:'])
    writer.writerow(['Greatest Decrease in Profits:'])