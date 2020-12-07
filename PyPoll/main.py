# import modules
import csv
import os

# set path for file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# define the function and have it accept the budget_data as sole parameter

    # set variables and assign values where possible 
    total_votes = 0 
    candidates = []
    votes = 0
    votes_khan = 0
    perc_khan = 0
    votes_correy = 0
    perc_correy = 0
    votes_li = 0
    perc_li = 0
    votes_otooley = 0
    perc_otooley = 0

for row in csvreader:

    total_votes = total_votes + 1

    candidates.append(row[2])
    
    #for candidates in csvreader
    votes.append(candidates)
    #votes_khan = votes_khan + int(votes_data[0]

print("Election Results")    
print("-------------------------")
print(f"Total Votes:")
print("-------------------------")
print(f"Khan: ")
print(f"Correy: ")
print(f"Li: ")
print(f"O'Tooley: ")
print("-------------------------")
print("Winner:")
print("-------------------------")