#Import the modules you need.
import os
import csv
#Set Path
csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_Pybank_Resources_Budget_data.csv')
#Define Dictionary
Valuedict = {}
Timedict = {}
#Open CSV File
with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
#Iterate and fill both dictionaries necessary
    for row in csvreader:
        Valuedict[row[0]] = int(row[1])
        Timedict[int(row[1])] = row[0]
#Define Values and calculations   
    Profitloss = Valuedict.values()
    Length = len(Valuedict)
    Total = sum(Profitloss)
    Average = round(sum(Profitloss) / len(Profitloss), 2)
    Largenumber = (max(Profitloss))
    Minnumber = (min(Profitloss))
    Monthmin = Timedict.get(Minnumber)
    Monthmax = Timedict.get(Largenumber)
#Print Analysis
print(f"""Financial Analysis
------------------
Total Months: {Length} months
Total: ${Total}
Average Change: ${Average}
Greatest Increase in Profits: {Monthmax} (${Largenumber})
Greatest Decrease in Profits: {Monthmin} (${Minnumber})"""
)
#Write the file
analysis = open('analysis/Analysis.txt', 'w')
analysis.write(f"""Financial Analysis
------------------
Total Months: {Length} months
Total: ${Total}
Average Change: ${Average}
Greatest Increase in Profits: {Monthmax} (${Largenumber})
Greatest Decrease in Profits: {Monthmin} (${Minnumber})"""
)