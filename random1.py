import random
names=['maher','hanan','masoun','lars','nizar','samer','maia','tarek']
def do(x):
    for i in range(x):
        print(random.choice(names), random.randrange(10))

do(5)