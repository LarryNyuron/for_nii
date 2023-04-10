import pandas as pd
import csv


dicti = {}


with open('test.csv', 'r', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
    #['461', '2000000', '361.814', '10.847']
    for rowe in spamreader:
        row = rowe[0].split(',')
        if row[0] not in dicti:
            dicti[row[0]] = {}
        else:
            a = dicti[row[0]]
            if row[1] not in a:
                a[row[1]] = [row[2]]
                dicti[row[0]] = a
            else:
                a[row[1]].append(row[2])
                dicti[row[0]] = a

f_sort = list(dicti['299'].keys())
t_sort = sorted(list(dicti.keys()))
F = [str(i) for i in sorted([int(i) for i in f_sort])]
T = [str(i) for i in sorted([int(i) for i in t_sort])]

f = open('output.csv', 'w')
f.write('Temp/Freq,' + ','.join(F) + '\n')
for i in T:
    row = i + ','
    for j in F:
        try:
            row = row + dicti[i][j][0] + ','
        except:
            row = row + ','
    f.write(row + '\n')






'''T = sorted([int(i) for i in t_sort])
'''