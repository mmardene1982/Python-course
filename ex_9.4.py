# 9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1: name = "mbox-short.txt"
handle = open(name)
count=dict()
max_email= None
max_count = None

for line in handle:
    line= line.strip()
    #if not line.startswith('From:'):continue
    words = line.split()
    #print(words)
    for x in words:
        count[x]= count.get(x, 0)+1
        if 'From:' in count:
            del count['From:']

for key, value in count.items():
    if max_count is None or value > max_count:
        max_email = key
        max_count = value
print('the most used word is:',max_email.upper(),'and it is mentioned :' ,max_count,"times")