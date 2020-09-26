#Import the modules you need.

import os
import csv

#Set Path

csvpath = os.path.join('resources','02-Homework_03-Python_Instructions_Pybank_Resources_Budget_data.csv')

#Open CSV

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    for row in csvreader:
        print(row)