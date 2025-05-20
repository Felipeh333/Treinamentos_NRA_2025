f = input().strip()

f1 = f.lower()

print(f1.count('a'))

print(f1.find('a'))

n=0
p=f1.find('a',n)

while (p>0):
    n=n+1
    p=f1.find('a',n)

print(n)
