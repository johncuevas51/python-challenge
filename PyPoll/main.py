import os
import csv

#Variables lists
total_votes = []
results_list = []
x = 'Raymon Anthony Doane'
Raymon_vote_count = 0
y = 'Diana DeGette'
Diana_count = 0
z = 'Charles Casper Stockham'
Charles_count = 0



#enter path
csvpath = os.path.join('Resources','election_data.csv')

#open CSV file
with open(csvpath) as csvfile:

#CSV reader specifies delimter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
 
#read the header row 
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")


# The total number of votes cast
    for i in csvreader:   
        total_votes.append(i[0])
        if i[2] == x:
            Raymon_vote_count = Raymon_vote_count + 1
        if i[2] == y:
            Diana_count = Diana_count + 1
        if i[2] == z:
            Charles_count = Charles_count + 1



    
    
#total votes 
count= len(total_votes)        

# A complete list of candidates who received votes

# The percentage of votes each candidate won
# Raymon
percent_raymon = (Raymon_vote_count/count) * 100
round_percent_raymon = round(percent_raymon, 3)

# Diana 
percent_diana = (Diana_count/count) * 100
round_percent_diana = round(percent_diana, 3)

# Chalres
percent_charles = (Charles_count/count) * 100
round_percent_charles = round(percent_charles, 3)

# The total number of votes each candidate won
print(f"Raymon number of votes won {Raymon_vote_count}")
print(f"Diana number of votes won {Diana_count}")
print(f"Charles number of votes won {Charles_count}")

# The winner of the election based on popular vote



winner=max(Raymon_vote_count,Diana_count,Charles_count)
(f"The winner of the votes is {winner}.")

output = f"""
Election Results
----------------------------
Total Votes: {count}
----------------------------
{x} : {(round_percent_raymon)}% , ({Raymon_vote_count})
{y} : {(round_percent_diana)}% , ({Diana_count})
{z} : {(round_percent_charles)}% , ({Charles_count})
----------------------------
Winner: Diana DeGette
"""
print(output)

with open("analysis/output_election.txt", "w") as output_file:
    output_file.write(output)