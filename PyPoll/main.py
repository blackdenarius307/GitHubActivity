#Import the modules you need.
import os
import csv
#Set Path
csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
#Define Dictionary
Votedict = {}
#Open CSV File
with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
#Iterate and fill the vote dictionary
    for row in csvreader:
        Votedict[row[0]] = row[2]
    TotalVotes= len(Votedict)
    print(TotalVotes)
    UniqueValue = set (val for dict in Votedict for val in dict.values())
    print(UniqueValue)    
        