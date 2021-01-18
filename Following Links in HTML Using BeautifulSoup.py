#Following Links in HTML Using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
count=input('Enter count: ')
count=int(count)
position=input('Enter position: ')
position=int(position)

# http://py4e-data.dr-chuck.net/known_by_Fikret.html

for c in range(count):
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    count = 0
    for tag in tags:
        count = count +1

        #stopping at desired position
        if count>position:
            break
        url = tag.get('href', None)
        name = tag.contents[0]

print(name)
