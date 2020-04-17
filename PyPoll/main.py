import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
outputpath = os.path.join("analysis", "results.csv")

total_k = 0
total_c = 0
total_l = 0
total_o = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
    # Creating new lists to store the data from the file and one to store
    # the candidate last names
    new_csvreader = list(csvreader)
    candidate_list = []

    total_votes = len(new_csvreader)
    
    # Storing the candidate last names in a new list
    for row in new_csvreader:
        candidate_list.append(str(row[2]))

    # Counting the votes for each candidate
    for row in new_csvreader:
        person = str(row[2])
        if person == "Khan":
            total_k = total_k + 1
        elif person == "Correy":
            total_c += 1
        elif person == "Li":
            total_l += 1
        elif person == "O'Tooley":
            total_o += 1

# Computing the percentages
percent_k = (total_k * 100) / total_votes
percent_c = (total_c * 100) / total_votes
percent_l = (total_l * 100) / total_votes
percent_o = (total_o * 100) / total_votes

# Finding out which one is the winner
winner_votes = max(total_k, total_c, total_l, total_o)

if winner_votes == total_k:
    winner = "Khan"
elif winner_votes == total_c:
    winner = "Correy"
elif winner_votes == total_l:
    winner = "Li"
elif winner_votes == total_o:
    winner = "O'Tooley"

# Printing results
print("Election Results")
print("---------------------------")
print(f"Total Votes: {total_votes}")
print("---------------------------")
print(f"Khan: {percent_k:.3f}% ({total_k})")
print(f"Correy: {percent_c:.3f}% ({total_c})")
print(f"Li: {percent_l:.3f}% ({total_l})")
print(f"O'Tooley: {percent_o:.3f}% ({total_o})")
print("---------------------------")
print(f"Winner: {winner}")
print("---------------------------")

# Storing results in a file
with open(outputpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",")

    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Khan: {percent_k:.3f}% ({total_k})"])
    csvwriter.writerow([f"Correy: {percent_c:.3f}% ({total_c})"])
    csvwriter.writerow([f"Li: {percent_l:.3f}% ({total_l})"])
    csvwriter.writerow([f"O'Tooley: {percent_o:.3f}% ({total_o})"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["---------------------------"])
