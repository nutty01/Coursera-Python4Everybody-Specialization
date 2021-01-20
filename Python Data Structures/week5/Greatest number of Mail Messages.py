

#Program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts =dict()
for line in handle:
    if line.startswith('From'):
        if not line.startswith('From:'):
            l=line.split()
            counts[l[1]] =counts.get(l[1],0)+1

max_value = max(counts.values())
print(max(counts,key=counts.get),max_value)   
