# import modules
import csv
import os

# set path for file
electioncsv = os.path.join("PyPoll", "Resources", "election_data.csv")

# open and read csv and skip the header
with open(electioncsv, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # set variables and assign values 
    total_votes = 0
    unique_candidates = []
    list_candidates = []
    candidate_votes = []
    perc_candidate_votes = []
    
    
    for row in csvreader:
        # Calculate the total number of votes cast
        total_votes = total_votes + 1

        # Obtain a list of unique candidates
        ##if row[2] not in unique_candidates:
            ##unique_candidates.append(row[2])
     
        # Make a list of all votes
        list_candidates.append(row[2])

       # Create a set of list_candidates to obtain unique values and print list of unique candidates
    set_candidates = set(list_candidates)
    unique_candidates = list(set_candidates)

        # For each unique candidate, add votes from the list of all votes to the candidates_vote list and count
    for candidate in unique_candidates:
        candidate_votes.append(list_candidates.count(candidate))
    
    

    # Determine percentages 
    perc_candidate_votes[:] = ([x / total_votes for x in candidate_votes])
    

    # determine most votes and corresponding name 
    most_votes = max(candidate_votes)
    winner = unique_candidates[candidate_votes.index(most_votes)]

print("Election Results")    
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for i in range(len(unique_candidates)):
        print(f"{unique_candidates[i]}: {perc_candidate_votes[i]} % {candidate_votes[i]}")  
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Set path for file to write to
output_path = os.path.join("PyPoll", "Analysis", "election_data.txt")

# Open and write
with open(output_path, 'w', newline='') as text_file:
    text_file.write(f"Election Results\n")    
    text_file.write(f"-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write(f"-------------------------\n")
    text_file.write(f"{unique_candidates}\n")
    text_file.write(f"{perc_candidate_votes} %\n")
    text_file.write(f"{candidate_votes}\n")
    text_file.write(f"-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write(f"-------------------------")
