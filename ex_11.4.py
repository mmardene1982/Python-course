import re
name = input('Enter file name: ')
if len(name)<1: name='regex_sum_185432.txt'
num_list=list()
count=0
fhandle= open(name)
for line in fhandle:
    line= line.rstrip()
    #print(line)
    numbers=re.findall('[0-9]+',line)
    if not numbers:continue
    #print(numbers)
    for i in numbers:
        num_list.append(i)
        count=count+1
print(num_list)
def int_sum(num_list):
    num_list_int= [int(x) for x in num_list]
    print(sum(num_list_int))
int_sum(num_list)