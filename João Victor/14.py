frase = input().strip()

def palin (a):

    x = a.replace(' ','').lower()
    y = str()

    for i in range(len(x)):
        y = x[i] + y

    verif = []

    for i in range(len(x)):
        if (x[i] != y[i]):
            verif.append(i)

    if(len(verif)) == 0:
        return('É um palíndromo')
    else:
        return('Não é um palíndromo')

print(palin(frase))