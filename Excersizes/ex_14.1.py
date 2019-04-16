import urllib.request, urllib.error, urllib.parse
import json

serviceURL= 'http://py4e-data.dr-chuck.net/comments_185437.json'
url= urllib.request.urlopen(serviceURL).read()
#print(url.decode())
data= url.decode()
js=json.loads(data)
jsS=json.dumps(data, indent=4)
count=[]
for k in js['comments']:
    counts=k['count']
    count.append(counts)
countI=[int(i) for i in count]
print(sum(countI))