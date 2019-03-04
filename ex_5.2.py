biggest = None
smallest = None
snum = input('Enter a number: ')
while snum:

    try:
        inum = float(snum)
    except:
        print('Invalid input type')
    if biggest is None:
        biggest = inum
        print(biggest)
