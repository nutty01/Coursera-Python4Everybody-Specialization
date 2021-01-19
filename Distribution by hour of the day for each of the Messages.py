#Program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.

handle = open("mbox-short.txt")

counts =dict()
for line in handle:
    if line.startswith('From'):
        if not line.startswith('From:'):
            l=line.split()
            s=l[5].split(':')
            for w in s[:1]:
                counts[w] =counts.get(w,0)+1
lst=list()
for key,val in counts.items():
    newtup=(key,val)
    lst.append(newtup)
    
lst=sorted(lst)

for key,val in lst:
    print(key,val)
