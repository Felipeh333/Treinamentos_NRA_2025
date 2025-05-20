import random

n1 = random.randint(1,100)

n2 = random.randint(1,100)

n3 = random.randint(1,100)

n4 = random.randint(1,100)

n5 = random.randint(1,100)

tup = n1, n2, n3, n4, n5

l=list(tup)

print(l, max(l), min(l))