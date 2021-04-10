#import 
import os
import csv

#joining path
pypoll_data = os.path.join('Resources', 'election_data.csv')

#open and read csv
with open(pypoll_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)

#define variables
  total_votes = 0
  khan_total = 0
  correy_total = 0
  li_total = 0
  otooley_total = 0

#read through each row after header and append into lists
  for row in csvreader:

#total votes
    total_votes = total_votes + 1

# A complete list of candidates who received votes
    if row[2] == "Khan":
      khan_total = khan_total + 1
    elif row[2] == "Correy":
      correy_total = correy_total + 1
    elif row[2] == "Li":
      li_total = li_total + 1
    elif row[2] == "O'Tooley":
      otooley_total = otooley_total + 1
  
# percentage of votes per candidate
    khan_p = (khan_total/total_votes) * 100
    correy_p = (correy_total/total_votes) * 100
    li_p = (li_total/total_votes) * 100
    otooley_p = (otooley_total/total_votes) * 100

# The winner of the election based on popular vote.

#print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print(f"Khan: ({khan_p})% ({khan_total})")
print(f"Correy: ({correy_p})% ({correy_total})")
print(f"Li: ({li_p})% ({li_total})")
print(f"O'Tooley: ({otooley_p})% ({otooley_total})")
print("-------------------------")
print("winner: ")
print("-------------------------")

#As an example, your analysis should look similar to the one below:

 # Election Results
  #-------------------------
  #Total Votes: 3521001
  #-------------------------
  #Khan: 63.000% (2218231)
  #Correy: 20.000% (704200)
  #Li: 14.000% (492940)
  #O'Tooley: 3.000% (105630)
  #-------------------------
  #Winner: Khan
  #-------------------------

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
#output_file = os.path.join('election_results.txt')
# with open(output_file, "w") as file:
  #file.write("Election Results")
  #file.write("\n")
  #file.write("----------------------------")
  #file.write("\n")
  #file.write(f"Total Votes: {total_votes}")
  #file.write("\n")
  #file.write("-------------------------")
  #file.write("\n")
  #file.write(f"Khan: ({khan_p})% ({khan_total})")
  #file.write("\n")
  #file.write(f"Correy: ({correy_p})% ({correy_total})")
  #file.write("\n")
  #file.write(f"Li: ({li_p})% ({li_total})")
  #file.write(f"O'Tooley: ({otooley_p})% ({otooley_total})")
  #file.write("-------------------------")
  #file.write("winner: ")
  #file.write("-------------------------")