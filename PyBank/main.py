#Modules
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)


    # for row in csvreader:
    #     print("CSV row: {0}".format(row))
    #print(csvreader)

    #csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    #for row in csvreader:
        #print(row)

    print(csvreader.line_num)

print("Financial Analysis")
print("----------------------------")    

#Total Numner of Months:
#print("Total Months: " )

#Net Total Amount of "Profit/Losses"
#print("Total: " + )

#Average of the changes in "Profit/Losses"
# print("Average Change: " + )

#Greatest increase in profits (date and amount)
# print("Greatest Increase in Profits: " + )

# Greatest decrease in losses (date and amount)
# print("Greatest Decrease in Profits: " + )