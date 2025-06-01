nome = []
idade = []
sexo = []

for i in range (4):

    nome.append(input(f"Nome da pessoa{i}:"))
    idade.append(int(input(f"Idade da pessoa{i}:")))
    sexo.append(input(f"Sexo da pessoa{i}:"))

media_idade = 0

for i in range(4):
    
    media_idade = idade[i] + media_idade

media_idade = media_idade / 4

count_mu18 = 0   
max_idade = 0

for n in range(4):
    if idade[n] > max_idade and sexo[n] == "masculino":
        max_idade = idade[n]
        j = n

    if sexo[n] == "feminino" and idade[i] < 20:
        count_mu18 += 1

print(f"Media de idade do grupo é : {media_idade}")
print(f"O homem mais velho é: {nome[j]}")
print(f"Numero de mulheres com menos de 20 anos: {count_mu18}")
