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
number_of_months_previous_profit_losses = 0

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
        
        # Calculate total number months
        total_number_of_months += 1

        # Calculate changes in profit/loss 
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
            number_of_months_previous_profit_losses += 1
      
        # Update previous profit/loss for the next iteration
        previous_profit_losses = profit_losses

        # Update the total profit/loss
        total_profit_losses += profit_losses

# Calculate the average change
average_change = round(total_changes / number_of_months_previous_profit_losses,2)

# Print the results
print(f'\nFinancial Analysis')
print(f'\n-----------------------------------------')
print(f'\nTotal Months: {total_number_of_months}')   
print(f'\nTotal: ${total_profit_losses}')
print(f'\nAverage Change: ${average_change}')
print(f'\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})')
print(f'\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})') 

###################################################################################################################
####################################### PRINT TXT #################################################################

# save the output file path    
output_file = os.path.join("Analysis", "Financial_Analysis.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as file:
    file.write("\nFinancial Analysis\n")
    file.write("\n--------------------------------\n")
    file.write(f"\nTotal Months: {total_number_of_months}\n")
    file.write(f"\nTotal: ${total_profit_losses}\n")
    file.write(f"\nAverage Change: ${average_change}\n")
    file.write(f"\nGreatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    file.write(f"\nGreatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})\n")