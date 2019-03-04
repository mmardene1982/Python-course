import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl, re
ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

URL= 'http://py4e-data.dr-chuck.net/comments_185434.html'
html= urllib.request.urlopen(URL, context=ctx)
html= html.read()
#print(html)
soup= BeautifulSoup(html,'html.parser')
lis=list()
tags= soup('span')
for tag in tags:
    #print('TAG:', tag)
    #print('URL:', tag.get('class', None))
    #print('Contents:', tag.contents[0])
    lis.append(tag.contents[0])
listI= [int(i) for i in lis]
    #print('AttributL=', tag.attrs)
print(sum(listI))