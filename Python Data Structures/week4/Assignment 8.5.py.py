# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 22:39:44 2020

@author: snsenel
"""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst = list()
for line in fh:
    if line.startswith('From'):
        if not line.startswith('From:'):
            #lst.append(line.rstrip().split())
            l=line.split()
            print(l[1])
            count=count+1
        
print("There were", count, "lines in the file with From as the first word")