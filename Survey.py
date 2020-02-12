import os
fd=os.open('Z-33.csv', os.O_RDWR|os.O_CREAT)
file= os.fdopen(fd, 'w')

handle= open("Z-33.txt")
for line in handle:
    line=line.strip()
    numbers=line.split()
    print(line)
    #depth= numbers[0]
   # inc=numbers[1]
   # azim=numbers[2]
   # print(depth,inc,azim)
   # file.write(depth+' '+inc+' '+azim+'\n')
