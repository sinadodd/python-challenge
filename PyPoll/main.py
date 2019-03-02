import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

total = 0
votes = {}
highest = 0
textfile = []

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total = total + 1
        if row[2] in votes:
            votes[row[2]] = votes[row[2]] + 1
        else:
            votes[row[2]] = 1
    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total))
    print("-------------------------")
    for entry in votes:
        percent = round((votes[entry] / total) * 100 , 3)
        print(entry + ": " + str(percent) + "% (" + str(votes[entry]) + ")")
        if votes[entry] > highest:
            highest = votes[entry]
            winner = entry
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
