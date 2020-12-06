# import modules
import csv
import os

# set path for file
csvpath = os.path.join('..', 'PyBank', 'Resources', 'election_data.csv')

# open and read csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

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