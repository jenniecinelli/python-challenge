#import 
import os
import csv

#joining path
pypoll_data = os.path.join('Resources', 'election_data.csv')

#open and read csv
with open(pypoll_data) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')
  csv_header = next(csvreader)

  #create lists for rows and define variables
  voter_ID = []
  county = []
  candidate = []

  #read through each row after header and append into lists
  for row in csvreader:
    voter_ID.append(row[0])
    county.append(row[1])
    candidate.append(row[2])
  
    # The total number of votes cast
    total_votes = len(voter_ID)

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.



#print
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
#print(candidate + ": " + (percent_votes) + (total_votes_each))
#print("winner: " + (winning_candidate))

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
