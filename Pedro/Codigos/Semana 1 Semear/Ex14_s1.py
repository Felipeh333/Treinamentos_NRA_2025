original = input()
original = original.lower()

def formata(original):
    frase = ""

    for i in original:

        if i != " ":
            frase = frase + i
    
    return frase

def inverte(frase):
    invertida = ""

    for i in range(len(frase)):

        invertida =  invertida + frase[len(frase) - i -1]

    return invertida

frase = formata(original)
invertida = inverte(frase)

if(frase == invertida):
    print("Palíndromo")

else:
    print("Não palíndormo")


