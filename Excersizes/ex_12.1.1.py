import urllib.request, urllib.error, urllib.parse, ssl, time
from bs4 import BeautifulSoup

# to deal with https websites
ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

# inputs
url= input('Enter URL: ')
if len(url)<1:
    url='http://py4e-data.dr-chuck.net/known_by_Fikret.html'
position= int(input('Enter Postion: '))
count= int(input('Enter Counts: '))
start= time.time()
# extract the url function and save it into a list
def my_func(url):
    html= urllib.request.urlopen(url, context=ctx).read()
    soup= BeautifulSoup(html, 'html.parser')
    tags=soup('a')
    mytags=tags[position-1]
    new_tag=mytags.get('href',None)
    print(new_tag)
    return new_tag
my_func(url)

# get the portion and counting and implement in the function
with open('url.txt', 'w') as fhandle:
    for i in range(count):
        url= my_func(url)
        fhandle.write(url+'\n')
    fhandle.close()
    end= time.time()
    print(end - start)