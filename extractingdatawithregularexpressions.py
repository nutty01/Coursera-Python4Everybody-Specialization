#Extracting Data with Regular Expressions

import re
hand = open('actual_data.txt')
sum=0
for line in hand:
    line = line.rstrip()
    stuff = re.findall('[0-9]+',line)
    for sublist in stuff:
        if sublist is None: continue
        sum+=int(sublist)
print(sum)
