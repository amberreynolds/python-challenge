#Modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

#net amount of profit and loss
Profit = []
months = []

#read through each row of data after header
for rows in csvreader:
    Profit.append(int(rows[1]))
    months.append(rows[0])

#revenue change
revenue_change = []

for x in range(1, len(Profit)):
    revenue_change.append((int(Profit[x]) - int(Profit[x-1])))
    
# avg revenue change
revenue_average = sum(revenue_change) / len(revenue_change)
    
#total length of months
total_months = len(months)

# greatest increase in revenue
greatest_increase = max(revenue_change)
# greatest decrease in revenue
greatest_decrease = min(revenue_change)

print("Financial Analysis")
print("----------------------------")    

#Total Numner of Months:
print("Total Months: " + str(total_months))

#Net Total Amount of "Profit/Losses"
print("Total: " + "$" + str(sum(Profit)))

#Average of the changes in "Profit/Losses"
print("Average Change: " + "$" + str(revenue_average))

#Greatest increase in profits (date and amount)
print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))

# Greatest decrease in losses (date and amount)
print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))

# Print to text file
file = open("output.txt","w")

file.write("Financial Analysis" + "\n")

file.write("...................................................................................." + "\n")

file.write("total months: " + str(total_months) + "\n")

file.write("Total: " + "$" + str(sum(P)) + "\n")

file.write("Average change: " + "$" + str(revenue_average) + "\n")

file.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")

file.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")

file.close()