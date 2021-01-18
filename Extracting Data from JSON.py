#Extracting Data from JSON

import urllib.request, urllib.parse, urllib.error
import json

url= 'http://py4e-data.dr-chuck.net/comments_1055080.json'

uh = urllib.request.urlopen(url)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')
js = json.loads(data)
sum=0
for item in js['comments']:
    num=int(item['count'])
    sum+=num
print(sum)
