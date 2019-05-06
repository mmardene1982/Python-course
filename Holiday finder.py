from bs4 import BeautifulSoup as bs
import urllib.request, urllib.parse, urllib.error, ssl
import os

ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

fd=os.open('Holidays.csv', os.O_RDWR|os.O_CREAT)
file= os.fdopen(fd, 'w')
linkUrl='https://www.visitoslo.com/en/oslo/practical-information/public-holidays/'
print('Retriving data from',linkUrl)
linkReq=urllib.request.urlopen(linkUrl, context=ctx)
linkRead=linkReq.read()
linkSoup=bs(linkRead, 'html.parser')
linkContainer=linkSoup.find('div',attrs={'class':'article-content'})
linkTable=linkContainer.findAll('table',attrs={'class':'selectable'})
linkTable=linkContainer.find('table',attrs={'class':'selectable'})
linkBody=linkTable.find('tbody')
rows=linkBody.findAll('tr')

for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    for i in cols:
        holiday,date19,date20=cols[0],cols[1],cols[2]
    print(holiday,date19,date20)
    file.write(holiday+','+date19+','+date20+'\n')
file.close()
