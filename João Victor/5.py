l = []
for i in range(3):
    l.append(int(input()))

l.sort()

if(l[2]>l[0]+l[1]):
    print('Não forma triângulo')

elif l[0]==l[1]==l[2]:
    print("Equilátero")

elif l[0]!=l[1]!=l[2]:
    print("Escaleno")

else:
    print("Isósceles")