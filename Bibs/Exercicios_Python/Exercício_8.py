# Desenvolvido por Beatriz Matias
# Exercício 8

soma_idade = 0
homem_mais_velho_idade = 0
homem_mais_velho_nome = ""
mulher_menos_20 = 0

for i in range(4):
    print(f"\nPessoa {i+1}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    sexo = input("Sexo (m/f): ")

    soma_idade += idade

    if sexo == "m":
        if idade > homem_mais_velho_idade:
            homem_mais_velho_idade = idade
            homem_mais_velho_nome = nome

    if sexo == "f" and idade < 20:
        mulher_menos_20 += 1

media_idade = soma_idade / 4

print("\n Média de idade do grupo:", media_idade)
print(" Homem mais velho:", homem_mais_velho_nome)
print(" Número de mulheres com menos de 20 anos:", mulher_menos_20)
