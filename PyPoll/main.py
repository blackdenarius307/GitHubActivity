#Import the modules you need.
import os
import csv
#Set Path
csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')
#Define Dictionary and Variables
Votedict = {}
KhanCounter = 0
OtooleyCounter = 0
CorreyCounter = 0
LiCounter = 0
Winner = 0
#Open CSV File
with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
#Iterate and fill the vote dictionary. Add to Counters.
    for row in csvreader:
        Votedict[row[0]] = str(row[2])
        if row[2] == 'Khan':
            KhanCounter += 1
        elif row[2] == 'Correy':
            CorreyCounter += 1
        elif row[2] == "O'Tooley":
            OtooleyCounter += 1
        elif row[2] == 'Li':
            LiCounter += 1
    if KhanCounter > CorreyCounter and KhanCounter > OtooleyCounter and KhanCounter > LiCounter:
        Winner = 'Khan'
    elif CorreyCounter > KhanCounter and CorreyCounter > OtooleyCounter and CorreyCounter > LiCounter:
        Winner = 'Correy'
    elif OtooleyCounter > KhanCounter and OtooleyCounter > CorreyCounter and OtooleyCounter > LiCounter:
        Winner = "O'Tooley"
    elif LiCounter > KhanCounter and LiCounter > CorreyCounter and LiCounter > OtooleyCounter:
        Winner= "Li"
#Make Calculations
    TotalVotes= len(Votedict)
    print(TotalVotes)
    Uniquevalues = set(Votedict.values())
    print(Uniquevalues)
    KhanPercent = round(KhanCounter / TotalVotes * 100, 2)
    OtooleyPercent = round(OtooleyCounter / TotalVotes * 100, 2)
    CorreyPercent = round(CorreyCounter / TotalVotes * 100, 2)
    LiPercent = round(LiCounter / TotalVotes * 100, 2)
#Print analysis
    print(f"""Election Results
    ----------------------
    Total Votes: {TotalVotes}
    ----------------------
    Khan: {KhanPercent}% ({KhanCounter})
    Correy: {CorreyPercent}% ({CorreyCounter})
    Li: {LiPercent}% ({LiCounter})
    O'Tooley {OtooleyPercent}% ({OtooleyCounter})
    ----------------------
    Winner = {Winner}
    ----------------------"""
    )
#Write file
# #Write the file
analysis = open('analysis/Analysis.txt', 'w')
analysis.write(f"""Election Results
----------------------
Total Votes: {TotalVotes}
----------------------
Khan: {KhanPercent}% ({KhanCounter})
Correy: {CorreyPercent}% ({CorreyCounter})
Li: {LiPercent}% ({LiCounter})
O'Tooley {OtooleyPercent}% ({OtooleyCounter})
----------------------
Winner = {Winner}
----------------------"""
)