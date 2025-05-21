# Desenvolvido por Beatriz Matias
# Exercício 18

valores = []

for i in range(5):
    numero = int(input(f"Digite o {i+1}º valor: "))
    valores.append(numero)

maior = max(valores)
menor = min(valores)

print("\nVocê digitou os valores:", valores)
print("Maior valor:", maior, "na posição", valores.index(maior))
print("Menor valor:", menor, "na posição", valores.index(menor))
