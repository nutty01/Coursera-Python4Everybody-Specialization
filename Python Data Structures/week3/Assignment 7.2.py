
## Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count=0
avg=0
total=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    total=float(line[20:])+total
avg=float(total)/count
print("Average spam confidence:",avg)
