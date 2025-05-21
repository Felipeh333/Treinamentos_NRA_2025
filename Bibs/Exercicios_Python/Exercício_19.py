# Desenvolvido por Beatriz Matias
# Exercício 19

valores = []
pares = []
impares = []

while True:
    numero = int(input("Digite um número (ou 0 para parar): "))
    if numero == 0:
        break
    valores.append(numero)

for n in valores:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("\n Todos os números digitados:", valores)
print(" Números pares:", pares)
print(" Números ímpares:", impares)



