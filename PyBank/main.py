import os
import csv

csvpath = os.path.join("Resources", "02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")
outputpath = os.path.join("analysis", "results.csv")

month_change = []
#decrease = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)
    
    # Creating new lists to store the data in the file and another to 
    # to store the data from the second column 
    new_csvreader = list(csvreader)
    profit_losses = []
    substracion_list = []

    # Storing the values of the file's second column 
    for row in new_csvreader:
        profit_losses.append(float(row[1]))    
    
    # for i in range(len(profit_losses)):
    #     if (i+1) == len(profit_losses):
    #         break
    #     substracion_list.append(profit_losses[i+1])

    for i in range(len(profit_losses)):
        if i == (len(profit_losses) - 1):
            break
        month_change.append(float(profit_losses[i+1]) - float(profit_losses[i]))
        
print(month_change)
print(type(month_change))
print(type(len(month_change)))

new_month = [float(i) for i in month_change]

total = sum(profit_losses)
print(total)
avg_change = sum(float(str(new_month))) / len(new_month)
print(avg_change)

print("Financial Analysis")
print("---------------------------")
print(f"Total Months: {len(profit_losses)}")
print(f"Total: ${total}")
print(f"Average  Change: ${avg_change}")
# print(f"Greatest Increase in Profits: {date_increase} (${increase})")
# print(f"Greatest Decrease in Profits: {date_decrease} (${decrease})")