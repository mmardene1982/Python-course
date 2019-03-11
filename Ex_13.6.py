import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# inputs link
url= input('Enter the link: ')
if len(url)< 1:
    url='http://py4e-data.dr-chuck.net/comments_185436.xml'
# handling https urls
ctx= ssl.create_default_context()
ctx.check_hostname= False
ctx.verify_mode= ssl.CERT_NONE

#read the url
html= urllib.request.urlopen(url, context=ctx)
data= html.read()

print('Retrieved', len(data), 'characters')
print(data.decode())
#convert srting into a tree
tree= ET.fromstring(data)
# find count element
counts= tree.findall('comments/comment/count')
# sum up the count total
countI= [int(count.text) for count in counts]
print('the count are:', str(len(counts)))
print('the total is:',sum(countI))





