# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 21:36:25 2019

@author: haras
"""

import plagarismCheck
import csv

def write_csv(rowA, rowB, rowC, rowD, rowE):
    with open("output.csv", 'w') as file:
        writer = csv.writer(file)
        writer.writerow(rowA)
        writer.writerow(rowB)
        writer.writerow(rowC)
        writer.writerow(rowD)
        writer.writerow(rowE) 

rowA = []
rowB = []
rowC = []
rowD = []
rowE = []

for x in range(1, 101):
    for y in range(0, 5):
        if y == 0:
            text_created = f"{x}.txt"
            text_original ="a.txt"
            rowA.append(plagarismCheck.some_func(text_original,text_created))
        elif y == 1:
            text_created = f"{x}.txt"
            text_original ="b.txt"
            rowB.append(plagarismCheck.some_func(text_original,text_created))
        elif y == 2:
            text_created = f"{x}.txt"
            text_original ="c.txt"
            rowC.append(plagarismCheck.some_func(text_original,text_created))
        elif y == 3:
            text_created = f"{x}.txt"
            text_original ="d.txt"
            rowD.append(plagarismCheck.some_func(text_original,text_created))
        elif y == 4:
            text_created = f"{x}.txt"
            text_original ="e.txt"
            rowE.append(plagarismCheck.some_func(text_original,text_created))
            
write_csv(rowA, rowB, rowC, rowD, rowE)
            
