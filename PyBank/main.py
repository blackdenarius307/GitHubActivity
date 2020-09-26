#Import the modules you need.

import os
import csv

#Set Path

csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_Pybank_Resources_Budget_data.csv')

#Define Variables

#Dates = []
#Totals = []
Mydict = {}

#Open CSV File

with open(csvpath, 'r') as csv_file:
    csvreader = csv.reader(csv_file, delimiter= ",")
    csv_header = next(csv_file)
#Iterate
    for row in csvreader:
        Mydict[row[0]] = {row[1]}
    
    Profitloss = Mydict.values()
    #Total = sum(Profitloss)
    print(Mydict)
    print(len(Mydict))
    print(Value)
    # print(Profitloss)
    #print(Total)






    
        
        #Dates.append(row[0])
        #Totals.append(row[1])
#Number of months
    #Numbmonth = len(Dates)
    #print(Numbmonth)

#Total Profit/Loss 
    #Profitloss = sum(Totals)
    #print(Profitloss)

#Largest



#Skip Header and define variables and list
    #Budgetlist = list(csvreader)
    #print(Budgetlist)
    #Totalchange = 0
    #csv_header = next(csv_file)
    #linecount= 0
    #Numbmonth= 0
    
        #print(csvreader)
        #Numbmonth += 1

#print(f'There are {Numbmonth} months in this dataset')
        