import urllib.request, urllib.parse, urllib.error
import json
from tkinter import *
import xml.etree.ElementTree as ET
import ssl, webbrowser

window=Tk()
window.title("Navigator")
window.iconbitmap(r"earth.ico")
T1= Entry(window)
T1.pack()


def text():
    ts=T1.get()
    print("Location is:",ts)
    return ts


ctx= ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode= ssl.CERT_NONE


def close_window():
    window.destroy()


def google():
    address = text()
    params = {"address":address}
    address = urllib.parse.urlencode(params,doseq=True)
    key = "&key=AIzaSyAyfDO8vzo3K0VQEdLmJ7A_RbgeeAB3OwY"
    url = "https://maps.googleapis.com/maps/api/geocode/xml?address="
    parse_url=url+address+key
    html = urllib.request.urlopen(parse_url, context=ctx).read()
    print("Retrieving:", parse_url)
    print("there is:", len(html),"char")
    data= html.decode()
    tree=ET.fromstring(data)
    lat=tree.findall("result/geometry/location/lat")
    lng=tree.findall("result/geometry/location/lng")
    status= tree.findall("status")
    if status[0].text != "OK":
        print("Unable to get the information")
        exit()
    print("Latitude:",lat[0].text)
    print("Longitude:",lng[0].text)
    grid = lat[0].text+","+lng[0].text
    place_id = tree.findall("result/place_id")
    output = "https://www.google.com/maps/search/?api=1&query="+grid+"&query_place_id="+place_id[0].text
    webbrowser.open(output, new=0, autoraise=True)


b1=Button(window, text="clickMe", comman=google).pack()
b2=Button(window, text="Exit",command=close_window).pack()


window.mainloop()