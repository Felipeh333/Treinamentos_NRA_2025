l = []

for i in range (5):
    l.append(int(input()))

pmax = ()

for i in range (5):
    if l[i] == max(l):
        pmax = i

pmin = ()
        
for i in range (5):
    if l[i] == min(l):
        pmin = i

print(max(l) ,min(l), pmax, pmin)