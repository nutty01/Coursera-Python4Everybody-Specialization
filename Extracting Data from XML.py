#Extracting Data from XML

import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error

url = input('Enter location: ')
uh = urllib.request.urlopen(url)
data = uh.read()
tree = ET.fromstring(data)

lst = tree.findall('comments/comment/count')

counts = tree.findall('.//count')
sum=0
for each in counts:
    num=int(each.text)
    sum+=num
print(sum)
