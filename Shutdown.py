import os
def SD():
    choice= input("Shutdown? (y/n)")
    if choice== "y":
        os.system("shutdown /r")

SD()