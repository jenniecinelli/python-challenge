

#import library
import os
import csv

#joining path
pybank_data = os.path.join('Resources', 'budget_data.csv')

#open and read csv
with open(pybank_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)


  #create lists for rows and define variables
  months = []
  profit_losses = []
  average_change = []

  #read through each row after header and append into lists
  for row in csvreader:
    months.append(row[0])
    profit_losses.append(int(row[1]))

  for p in range(len(profit_losses)-1):
#The average of the changes in "Profit/Losses" over the entire period
    average_change.append((profit_losses[p+1] - profit_losses[p]))

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = max(average_change)

#The greatest decrease in losses (date and amount) over the entire period
greatest_decrease = min(average_change)

max_month = average_change.index(max(average_change)) + 1
min_month = average_change.index(min(average_change)) + 1

#print financial analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(months)}")
print(f"Total: ${sum(profit_losses)}")
print(f"Average Change: {(sum(average_change) / len(average_change))}")
print(f"Greatest Increase in Profits: {months[max_month]} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {months[min_month]} (${str(greatest_decrease)})")


#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
output_file = os.path.join('financial_analysis.txt')
with open(output_file, "w") as file:
  file.write("Financial Analysis")
  file.write("\n")
  file.write("----------------------------")
  file.write("\n")
  file.write(f"Total Months: {len(months)}")
  file.write("\n")
  file.write(f"Total: ${sum(profit_losses)}")
  file.write("\n")
  file.write(f"Average Change: {(sum(average_change) / len(average_change))}")
  file.write("\n")
  file.write(f"Greatest Increase in Profits: {months[max_month]} (${str(greatest_increase)})")
  file.write("\n")
  file.write(f"Greatest Decrease in Profits: {months[min_month]} (${str(greatest_decrease)})")