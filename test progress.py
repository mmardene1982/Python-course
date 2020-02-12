
import fbchat
from fbchat import Client
from getpass import getpass

import random, time

username= "maher.mardini1"
client= fbchat.Client(username, getpass())
name= str(input("name: "))
friends= client.searchForUsers(name)
friend=friends[0]
msg=["\U0001f600","\U0001F606","\U0001F923",]
for i in range(15):
    sent=client.send(fbchat.models.Message(random.choice(msg)),friend.uid)
    time.sleep(1)


if sent:
    print("all good")
    client.logout()