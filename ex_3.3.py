
score = input("Enter Score: ")

try:
    scoreF= float(score)

except:
    "Your entry is not acceptable"
    quit()

if scoreF >1:
    print("Your entry is out of range")
    quit()

elif scoreF >=0.9:
    print ("A")
elif scoreF>=0.8:
    print ("B")
elif scoreF >=0.7:
    print("C")
elif scoreF >=0.6:
    print("D")
elif scoreF < 0.6:
    print("F")

