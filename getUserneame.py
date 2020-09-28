import json
import socket
import getpass
from urllib.request import urlopen
username = getpass.getuser()
print('USERNAME     :   ', username)

hostname = socket.gethostname()
print('HOSTNAME     :   ', hostname)

machineIP = socket.gethostbyname(hostname)
print('IP ADDRESS   :   ', machineIP)

url = "http://ipinfo.io/json"
response = urlopen(url)

data = json.load(response)

print('PUBLIC IP    :   ', data['ip'])
print('CITY         :   ', data['city'])
print('REGION       :   ', data['region'])
print('LOCATION     :   ', data['loc'])
print('POSTAL       :   ', data['postal'])
print('TIME ZONE    :   ', data['timezone'])
