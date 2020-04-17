import os
import csv

csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
outputpath = os.path.join("analysis", "results.csv")

month_change = []
dates = []
profit_losses = []
substracion_list = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
    # Creating a new list to store the data in the file
    new_csvreader = list(csvreader)
    
    # Storing the values of the file's first and second column 
    for row in new_csvreader:
        profit_losses.append(float(row[1]))
        dates.append(str(row[0]))

    # Computing the monthly changes 
    for i in range(len(profit_losses)):
        if i == (len(profit_losses) - 1):
            break
        month_change.append(float(profit_losses[i+1]) - float(profit_losses[i]))

# Computing the Total
total = sum(profit_losses)

# Computing the average change
sum_change = 0
for i in range(len(month_change)):
    sum_change += float(month_change[i])

avg_change = sum_change/len(month_change)

# Computing the biggest increase and decrease
increase = max(month_change)
decrease = min(month_change)

# Finding the index to match it with the date
for i in range(len(month_change)):
    if increase == month_change[i]:
        increase_index = i
    if decrease == month_change[i]:
        decrease_index = i

# printing the results
print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(profit_losses)}")
print(f"Total: ${total}")
print(f"Average  Change: ${avg_change:.2f}")
print(f"Greatest Increase in Profits: {dates[increase_index+1]} (${increase})")
print(f"Greatest Decrease in Profits: {dates[decrease_index+1]} (${decrease})")

# Storing results in a file
with open(outputpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter = ",")

    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["---------------------------"])
    csvwriter.writerow([f"Total Months: {len(profit_losses)}"])
    csvwriter.writerow([f"Total: ${total}"])
    csvwriter.writerow([f"Average  Change: ${avg_change:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {dates[increase_index+1]} (${increase})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {dates[decrease_index+1]} (${decrease})"])

 