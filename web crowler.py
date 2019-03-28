from bs4 import BeautifulSoup as bs
import urllib.request, urllib.parse, urllib.error, ssl
import os 


ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE
fd=os.open('products.csv', os.O_RDWR|os.O_CREAT)

f= os.fdopen(fd,'w')
headres= "Product Name, Price\n"
f.write(headres)
url='https://www.finn.no/bap/forsale/search.html?lat=58.91976&lon=5.70943&page='
url1='&q=apple+iphone&search_type=SEARCH_ID_BAP_ALL&sub_category=1.93.3217'
pages=input("Enter how many pages you want to check: ")
pages=int(pages)
for page in range(pages):
    url=url+str(page)+url1
    url_req= urllib.request.urlopen(url, context=ctx)
    url_read=url_req.read()
    url_req.close()

    soup= bs(url_read, 'html.parser')
    containers= soup.findAll("div", attrs={"class":"ads__unit"})
    print(len(containers))
    count=0
    for container in containers:
        title_container=container.find("a", attrs={"class":"ads__unit__link"})
        price_container= container.find("div", attrs={"class":"ads__unit__img__ratio__price"})
        if not title_container : continue
        if not price_container: continue
        price_tag= price_container.text.strip()
        product_name=title_container.text.strip()
        print("product Name:", product_name)
        print("product price:", price_tag)
        f.write(product_name.replace(",","|") +","+price_tag+"\n")
f.close()

