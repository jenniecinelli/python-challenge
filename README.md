python-challenge

Before You Begin:

1. Create a new repository for this project called `python-challenge`. **Do not add this homework to an existing repository**.

2. Clone the new repository to your computer.

3. Inside your local git repository, create a directory for both of the  Python Challenges. Use folder names corresponding to the challenges: **PyBank** and  **PyPoll**.

4. Inside of each folder that you just created, add the following:

5. A new file called `main.py`. This will be the main script to run for each analysis.

6. A "Resources" folder that contains the CSV files you used. Make sure your script has the correct path to the CSV file.

7. An "analysis" folder that contains your text file that has the results from your analysis.

8. Push the above changes to GitHub or GitLab.

PyBank:

[Revenue](Images/revenue-per-lead.png)

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:

1. The total number of months included in the dataset

2. The net total amount of "Profit/Losses" over the entire period

3. The average of the changes in "Profit/Losses" over the entire period

4. The greatest increase in profits (date and amount) over the entire period

5.  The greatest decrease in losses (date and amount) over the entire period

6. As an example, your analysis should look similar to the one below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

7.  In addition, your final script should both print the analysis to the terminal and export a text file with the results.

PyPoll:

[Vote Counting](Images/Vote_counting.png)

In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.

You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyzes the votes and calculates each of the following:

1. The total number of votes cast

2. A complete list of candidates who received votes

3. The percentage of votes each candidate won

4. The total number of votes each candidate won

5. The winner of the election based on popular vote.

As an example, your analysis should look similar to the one below:

  ```text
  Election Results
  -------------------------
  Total Votes: 3521001
  -------------------------
  Khan: 63.000% (2218231)
  Correy: 20.000% (704200)
  Li: 14.000% (492940)
  O'Tooley: 3.000% (105630)
  -------------------------
  Winner: Khan
  -------------------------
  ```

6. In addition, your final script should both print the analysis to the terminal and export a text file with the results.
