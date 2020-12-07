# import modules
import csv
import os

# set path for file
budgetcsv = os.path.join("PyBank", "Resources", "budget_data.csv")

# open and read csv and skip the header
with open(budgetcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # set variables and assign values
    
    total_months = 0
    net_total = 0
    previous_pl = 0
    change_pl = 0
    track_change_pl = 0
    average_changes = []
    max_increase = 0
    max_decrease = 0
    
    # read through each row after the header
    for row in csvreader:

    # Calculate the total number of months included in the dataset NEED TO ADD ONE MORE?
        total_months = total_months + 1

    # Calculate net total amount of "Profit/Losses" over the entire period CONFIRM TOTAL AMOUNT
        net_total = net_total + int(row[1])

    # Calculate the average of the changes in "Profit/Losses" over the entire period

        pl = int(row[1])

        if total_months == 1:
            previous_pl = pl
        else:
            change_pl = pl - previous_pl
            track_change_pl = track_change_pl + change_pl
            previous_pl = int(row[1])

    # Calculate the greatest increase and decrease in profits (date and amount) over the entire period
        if change_pl > max_increase:
            max_increase = change_pl
            date_increase = row[0]
        
        if change_pl < max_decrease:
            max_decrease = change_pl
            date_decrease = row[0]

# calculate the average, taking into account the number of change_pl is less than the amount
average_changes = round(track_change_pl/(total_months - 1),2)

# prepare output summary to print
print("Financial Analysis")
print(f"----------------------------")
print(f"Total months: {total_months}")
print(f"Total: $ {net_total}")
print(f"Average Change $ {average_changes}")
print(f"Greatest Increase in Profits: {date_increase} (${max_increase})")
print(f"Greatest Decrease in Profits: {date_decrease} (${max_decrease})")

# set path for file to write to
outputpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# open and write
with open(output_path, 'w', newline='') as text_file:
    text_file.write("Financial Analysis")
    text_file.write(f"----------------------------")
    text_file.write(f"Total months: {total_months}")
    text_file.write(f"Total: $ {net_total}")
    text_file.write(f"Average Change $ {average_changes}")
    text_file.write(f"Greatest Increase in Profits: {date_increase} (${max_increase})")
    text_file.write(f"Greatest Decrease in Profits: {date_decrease} (${max_decrease})")

