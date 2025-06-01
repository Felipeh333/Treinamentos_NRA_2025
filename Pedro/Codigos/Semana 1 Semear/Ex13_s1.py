frase = input("Frase: ")
frase = frase.lower()
posição_final = -1

for i in range(len(frase)):
    if frase[i] == "a":
        posição_final = i

if posição_final == -1:
    print("Não há letras A na frase")

else:
    print(f"Número de vezes que aparece a letra A na frase: {frase.count("a",0,len(frase))}")
    print(f"Primeiro A é no carractere {frase.find('a')}")
    print(f"Ultimo A é no carractere {posição_final}")
