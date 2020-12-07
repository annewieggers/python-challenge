# import modules
import csv
import os

# set path for file
budgetcsv = os.path.join("Resources", "budget_data.csv")

# open and read csv
with open(budgetcsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# Read the header row first (skip this part if there is no header)
    #csv_header = next(csvreader)

            # set variables and assign values where possible
            # total_months = 0
            #net_amount = 0
            #pl = int(row[1]) 
            #previous_pl = 0
            #change_pl = 0
            #total_change = []
            #average_change = 0
            #greatest_increase = []
            #greatest_decrease = []


# Read through each row of data after the header
    for row in csvreader:

        # calculate the total months
        #total_months = total_months + 1

        # calculate the net amount of profit/loss
        #net_amount.append(row[1]) - when is .append required? always or only when working with a list?
        #net_amount = net_amount + int(row[1])

        # calculate the average of the change in profit/loss
        #change_pl = pl - previous_pl

        # add up revenue changes
        #total_change.append(change_pl)
        #total_change = sum(change_pl)

        #average_change = total_change
        # total_change/len(total_change)

        # reset the pl to become the previous_pl
        # previous_pl = int(row[1])
        
        # determine greatest increase
        #greatest_increase = max(average_change)
        #if average_change > 

        # determine greatest decrease
        #greatest_decrease = max(average_change)




# create an output file

output_path = os.path.join("output", "new.csv")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
        #print("Financial Analysis")
        #print(f"----------------------------")
        #print(f"Total months str(total_months))
        #print(f"Total")
        #print(f"Average change $str(average_changes)")
        #print(f"Greatest Increase in Profits str(greatest_increase)")
        #print(f"Greatest Decrease in Profits str(greated_decrease)")