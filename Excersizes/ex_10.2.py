# 10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages.
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lis=list()
count = dict()
for line in handle:
    line = line.rstrip()
    #print(line)
    if not line.startswith('From '): continue
    #print(line)
    comma= ':'
    comma_pos= line.find(comma,0,len(line))
    end_pos=line.find('2008',0,len(line))
    value= line[comma_pos-2:end_pos-1]
    #print(value)
    hrs= value.split(':')
    hours= hrs[0]
    lis.append(hours)
for i in lis:
    count[i]=count.get(i,0)+1
value = sorted(count.items())
for k,v in value:
    print(k,v)

