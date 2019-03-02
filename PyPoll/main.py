import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

totalMonths = 0
total = 0
greatestinc = 0
greatestdec = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)

    for row in csvreader:
        totalMonths = totalMonths + 1
        total = total + int(row[1])
        if int(row[1]) > greatestinc:
            greatestinc = int(row[1])
            greatestincMonth = row[0]
        if int(row[1]) < greatestdec:
            greatestdec = int(row[1])
            greatestdecMonth = row[0]

average = round((total / totalMonths),2)

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(totalMonths))
print("Total: $" + str(total))
print("Average Change: $" + str(average))
print("Greatest Increase in Profits: " + str(greatestincMonth) + " ($" + str(greatestinc) + ")")
print("Greatest Decrease in Profits: " + str(greatestdecMonth) + " ($" + str(greatestdec) + ")")

output_file = os.path.join("Results_PyBank.txt")
with open(output_file, "w", newline="") as textfile:
    writer = csv.writer(textfile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["----------------------------"])
    writer.writerow(["Total Months: " + str(totalMonths)])
    writer.writerow(["Total: $" + str(total)])
    writer.writerow(["Average Change: $" + str(average)])
    writer.writerow(["Greatest Increase in Profits: " + str(greatestincMonth) + " ($" + str(greatestinc) + ")"])
    writer.writerow(["Greatest Decrease in Profits: " + str(greatestdecMonth) + " ($" + str(greatestdec) + ")"])