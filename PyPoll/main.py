#PyPoll

import os
import csv
import sys

header_store = []
cand = []
linecount = 0
votesCCS = 0
votesDD = 0
votesRAD = 0

CCS = "Charles Casper Stockham"
DD = "Diana DeGette"
RAD = "Raymon Anthony Doane"

# putting file path in a variable
poll_path = os.path.join('Resources','election_data.csv')


# opening csv file and formatting for reading
with open(poll_path) as poll_file:
    poll_reader = csv.reader(poll_file, delimiter=',')
    
    # skipping headers
    for y in poll_reader:
        
        #stores and skips header
        if linecount == 0:
            header_store = y
            linecount += 1
         #placing candidates in python 'file'
        else:
            cand.append(y[2])

votes = len(cand) #total number of votes

# finds total votes for each candidate
for i in range(votes):

    if cand[i] == CCS:
        votesCCS += 1
    
    elif cand[i] == DD:
        votesDD += 1

    elif cand[i] == RAD:
        votesRAD += 1

    else:
        pass

#finds vote percentage for each candidate
CCSper = round(((votesCCS/votes)*100),3)
DDper = round(((votesDD/votes)*100),3)
RADper = round(((votesRAD/votes)*100),3)

#finds winner of election
if votesCCS > votesDD and votesCCS > votesRAD:
    winner = CCS
elif votesDD > votesCCS and votesDD > votesRAD:
    winner = DD
else:
    winner = RAD

#stores original standard output
original_stdout = sys.stdout

# writes analysis to a text file
with open('analysis.txt','w') as file1:
    sys.stdout = file1

    print("Election Results")
    print("-----------------------")
    print("Total Votes:", votes)
    print("-----------------------")
    print(f"{CCS}: {CCSper}% ({votesCCS})")
    print(f"{DD}: {DDper}% ({votesDD})")
    print(f"{RAD}: {RADper}% ({votesRAD})")
    print("------------------------")
    print(f"Winner: {winner}")
    print("------------------------")


    sys.stdout = original_stdout

print("Election Results")
print("-----------------------")
print("Total Votes:", votes)
print("-----------------------")
print(f"{CCS}: {CCSper}% ({votesCCS})")
print(f"{DD}: {DDper}% ({votesDD})")
print(f"{RAD}: {RADper}% ({votesRAD})")
print("------------------------")
print(f"Winner: {winner}")
print("------------------------")

        
