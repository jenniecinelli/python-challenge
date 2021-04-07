
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
  
  net_total = 0

  #read through each row after header and append into lists
  for row in csvreader:
    months.append(row[0])
    profit_losses.append(row[1])

#total number of months
  total_months = len(months)

#The net total amount of "Profit/Losses" over the entire period
  for nloop in range(total_months):
    net_total = net_total + int(profit_losses[nloop])

#The average of the changes in "Profit/Losses" over the entire period

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

#print financial analysis
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(total_months))
print("Total: " + "$" + str(net_total))
#print("Average Change: " + )
#print("Greatest Increase in Profits: " + )
#print("Greatest Decrease in Profits" +)

#As an example, your analysis should look similar to the one below:

  #text
  #Financial Analysis
  #----------------------------
  #Total Months: 86
  #Total: $38382578
  #Average  Change: $-2315.12
  #Greatest Increase in Profits: Feb-2012 ($1926159)
  #Greatest Decrease in Profits: Sep-2013 ($-2196167)

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.