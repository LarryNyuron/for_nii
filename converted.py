import pandas as pd
import csv


with open('test.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    for row in spamreader:
        print(', '.join(row))
