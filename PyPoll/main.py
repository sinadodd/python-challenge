import os
import csv

total = 0
votes = {}
highest = 0
textfile = []

csvpath = os.path.join("..", "Resources", "election_data.csv")
output_file = os.path.join("Results_PyPoll.txt")

with open(output_file, "w", newline="") as textfile:
    writer = csv.writer(textfile)
    writer.writerow(["Election Results"])
    writer.writerow(["-------------------------"])

    with open(csvpath, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)
        for row in csvreader:
            total = total + 1
            if row[2] in votes:
                votes[row[2]] = votes[row[2]] + 1
            else:
                votes[row[2]] = 1
        writer.writerow(["Total Votes: " + str(total)])
        writer.writerow(["-------------------------"])
        print("Election Results")
        print("-------------------------")
        print("Total Votes: " + str(total))
        print("-------------------------")
        for entry in votes:
            percent = round((votes[entry] / total) * 100 , 3)
            print(entry + ": " + str(percent) + "% (" + str(votes[entry]) + ")")
            writer.writerow([entry + ": " + str(percent) + "% (" + str(votes[entry]) + ")"])
            if votes[entry] > highest:
                highest = votes[entry]
                winner = entry
        writer.writerow(["-------------------------"])
        writer.writerow(["Winner: " + winner])
        writer.writerow(["-------------------------"])

print("-------------------------")
print("Winner: " + winner)
print("-------------------------")
