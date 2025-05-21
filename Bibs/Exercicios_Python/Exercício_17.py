# Desenvolvido por Beatriz Matias
# Exercício 17

from random import randint

numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))

print("Números gerados:", end=" ") # lerbrar que o end=" " evita que pule uma linha entre os números
for n in numeros:
    print(n, end=" ")

print("\nMaior número:", max(numeros))
print("Menor número:", min(numeros))

