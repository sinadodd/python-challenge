import os
import csv

csvpath = os.path.join("..", "Resources", "election_data.csv")

total = 0
votes = {}


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    for row in csvreader:
        total = total + 1
        if row[2] in votes:
            votes[row[2]] = votes[row[2]] + 1
        else:
            votes[row[2]] = 1
    for entry in votes:
        print(entry)
        print(votes[entry])


print(votes)
print(total)



"""The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:


  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------"""