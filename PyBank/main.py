#Import the modules you need.

import os
import csv

#Set Path

csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_Pybank_Resources_Budget_data.csv')

#Define Dictionary

Mydict = {}

#Open CSV File

with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
#Iterate
    for row in csvreader:
        Mydict[row[0]] = int(row[1])
    
    Profitloss = Mydict.values()
    Total = sum(Profitloss)

    print(Profitloss)
    print(Total)
    print(sum(Profitloss) / len(Profitloss))
    Largenumber = (max(Profitloss))
    Minnumber = (min(Profitloss))
    print(Minnumber)
    print(Largenumber)
    print(Minnumber in Mydict)