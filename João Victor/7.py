r = ()
s = []
i = []

#input

while r!='n':
    print('Digite o sexo (h/m) e idade ')
    s.append(input().strip())
    i.append(int(input()))

    print('Deseja continuar?(y/n)')
    r = input().strip()

#maiores de idade

m = int()

for k in range (len(i)):
    if i[k]>=18:
        m = m+1

#sexo

nh = int()

for k in range (len(s)):
    if s[k]=='h':
        nh = nh+1

#mulher com menos de 20 anos

m1 = int()

for k in range (len(s)):
    if s[k]=='m':
        if i[k]<20:
            m1=m1+1

print(m,nh,m1)