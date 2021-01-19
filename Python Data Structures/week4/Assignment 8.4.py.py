# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:30:31 2020

@author: snsenel
"""

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    #print(line.rstrip().split())
    lst.append(line.rstrip().split())

total = []
for i in lst:
    total += i

total=list(dict.fromkeys(total))
total.sort()

print(total)