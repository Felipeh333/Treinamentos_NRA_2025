soma_idade = 0
idade_mais_velho = 0
nome_mais_velho = ''
mulheres_menos_20 = 0

for i in range(4):
    nome = input(f"Nome {i + 1}: ")
    
    idade = int(input(f"Idade {i + 1}: "))
    soma_idade += idade
    
    sexo = input(f"Sexo {i + 1} (M/F): ")
    
    if idade > idade_mais_velho and sexo == 'M':
        nome_mais_velho = nome
        idade_mais_velho = idade
    
    if idade < 20 and sexo == 'F':
        mulheres_menos_20 += 1
    
print("Homem mais velho:", nome_mais_velho)
print("Média das idades:", soma_idade / 4)
print("Mulheres menores que 20:", mulheres_menos_20)
