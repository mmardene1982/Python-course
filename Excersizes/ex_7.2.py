# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file,
# looking for lines of the form:
# X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines and compute the average of those values
# and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter
# mbox-short.txt as the file name.

# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
fh = open('mbox-short.txt')
count = 0
tot= 0
for line in fh:
    line = line.strip()
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count + 1
    sub = ':'
    numPos = line.find(sub)
    value = line[numPos+2:]
    tot =tot + float(value)
    avrg = tot / count
print('The count is:', count)
print('The total is:', tot)
print("Average spam confidence:", avrg)


