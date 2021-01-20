name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

di=dict()
for lin in handle:
    lin=lin.rstrip()
    wds=lin.split()
    for w in wds:
        #idiom: retrieve/create/update counter
        di[w]=di.get(w,0)+1

largest=-1
theword=None
for k,v in di.items():
    if v>largest:
        largest=v
        theword=k  #capture/remember the key that was largest
print(theword,largest)
    
    
    
    
    
