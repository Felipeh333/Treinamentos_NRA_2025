r = ()
n = []
s = []
i = []

#input

for k in range (4):
    print('Digite nome, sexo (h/m) e idade ')
    n.append(input().strip())
    s.append(input().strip())
    i.append(int(input()))

#media

media = int()

for k in range (4):
    media = media+i[k]

media = media/4

#homem mais velho

idademax = int()
nome = str()

for k in range(4):
    if s[k] =='h':
        if(idademax<i[k]):
            idademax=i[k]

for k in range(4):
    if s[k] == 'h':
        if i[k] == idademax:
            nome = n[k]

#mulheres com menos de 20

m1 = int()

for k in range (4):
    if s[k] == 'm':
        if i[k]<20:
            m1 = m1+1

print(media,nome,m1)